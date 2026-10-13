"""
dashboard.py  --  FastHTML Employee Performance Dashboard
Routes:
  GET /                   Index / navigation page
  GET /employee?id=<int>  Single-employee dashboard
  GET /team?id=<int>      Team dashboard
Run: python dashboard.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import matplotlib
matplotlib.use("Agg")

from fasthtml.common import (
    fast_app, serve,
    Html, Head, Body, Title, Link,
    Div, H1, H2, H3, P, A, Span,
    Form, Select, Option, Button,
)

from employee_events import Employee, Team
from utils import load_model, ROOT
from base_components import BaseComponent, Dropdown, DataTable, MatplotlibViz
from combined_components import CombinedComponent, FormGroup

# ── ML model ─────────────────────────────────────────────────────────────────
ml_model = load_model()

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS_PATH = ROOT / "assets" / "report.css"
css_headers = [Link(rel="stylesheet", href="/assets/report.css")] if CSS_PATH.exists() else []


# =============================================================================
#  Custom BaseComponent subclasses
# =============================================================================

class PageHeader(BaseComponent):
    """Displays the entity name as a top-level heading with a back link."""

    def build_component(self, entity_id, model):
        label = "Employee" if model.name == "employee" else "Team"
        name  = model.username(entity_id)
        return Div(
            H1(f"{label}: {name}", cls="page-title"),
            A("\u2190 Back to Home", href="/", cls="back-link"),
            cls="page-header",
        )


class RecruitmentRisk(BaseComponent):
    """Predicts and displays recruitment-risk probability (colour-coded)."""

    def build_component(self, entity_id, model):
        data = model.model_data(entity_id)

        if data is None or data.empty or data[["positive_events", "negative_events"]].isnull().all().all():
            return Div(H3("Recruitment Risk"), P("Insufficient data for prediction."), cls="risk-container")

        features = data[["positive_events", "negative_events"]].fillna(0)
        probs     = ml_model.predict_proba(features)[:, 1]
        avg_risk  = float(probs.mean())

        if avg_risk >= 0.70:
            risk_cls, label = "risk-high",   "High"
        elif avg_risk >= 0.40:
            risk_cls, label = "risk-medium", "Medium"
        else:
            risk_cls, label = "risk-low",    "Low"

        return Div(
            H3("Recruitment Risk"),
            Div(
                Span(f"{avg_risk:.1%}", cls=f"risk-score {risk_cls}"),
                Span(f" ({label})",     cls="risk-label"),
                cls="risk-display",
            ),
            cls="risk-container",
        )


class EventLineChart(MatplotlibViz):
    """Line chart showing positive/negative events over time."""

    def visualization(self, data, entity_id, model):
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(12, 5))
        if data is not None and not data.empty:
            n = len(data)
            x = range(n)
            ax.plot(x, data["positive_events"], label="Positive Events",
                    color="#2196F3", marker="o", linewidth=2, markersize=5)
            ax.plot(x, data["negative_events"],  label="Negative Events",
                    color="#F44336", marker="o", linewidth=2, markersize=5)
            step = max(1, n // 10)
            ax.set_xticks(list(x)[::step])
            ax.set_xticklabels(data["event_date"].iloc[::step], rotation=45, ha="right", fontsize=8)
            title = ("Employee Performance Events Over Time"
                     if model.name == "employee"
                     else "Team Performance Events Over Time")
            ax.set_title(title, fontsize=13, fontweight="bold")
            ax.set_ylabel("Number of Events")
            ax.legend(); ax.grid(True, alpha=0.25)
        else:
            ax.text(0.5, 0.5, "No event data available",
                    ha="center", va="center", transform=ax.transAxes, fontsize=12, color="grey")
        fig.tight_layout()
        return fig


class EventDataTable(DataTable):
    """Table of per-date event counts (inherits DataTable behaviour)."""
    pass


# =============================================================================
#  CombinedComponent page layouts
# =============================================================================

class EmployeeDashboard(CombinedComponent):
    children = [PageHeader(), RecruitmentRisk(), EventLineChart(), EventDataTable()]

    def __call__(self, entity_id, model):
        return self.outer_div(self.call_children(entity_id, model),
                              {"cls": "dashboard employee-dashboard"})


class TeamDashboard(CombinedComponent):
    children = [PageHeader(), RecruitmentRisk(), EventLineChart(), EventDataTable()]

    def __call__(self, entity_id, model):
        return self.outer_div(self.call_children(entity_id, model),
                              {"cls": "dashboard team-dashboard"})


# =============================================================================
#  Singletons
# =============================================================================

employee_model = Employee()
team_model     = Team()
employee_page  = EmployeeDashboard()
team_page      = TeamDashboard()

# =============================================================================
#  FastHTML app + routes
# =============================================================================

app, rt = fast_app(hdrs=css_headers)


@rt("/")
def index():
    employee_options = [Option(n, value=str(i)) for i, n in employee_model.names()]
    team_options     = [Option(n, value=str(i)) for i, n in team_model.names()]

    return Html(
        Head(Title("Employee Performance Dashboard"), *css_headers),
        Body(
            Div(
                H1("Employee Performance Dashboard", cls="main-title"),
                P("Monitor performance events and recruitment risk for employees or teams.", cls="subtitle"),
                Div(
                    H2("Employee View"),
                    Form(Select(*employee_options, name="id"), Button("View Employee", type="submit"),
                         action="/employee", method="get", cls="selector-form"),
                    cls="selector-card",
                ),
                Div(
                    H2("Team View"),
                    Form(Select(*team_options, name="id"), Button("View Team", type="submit"),
                         action="/team", method="get", cls="selector-form"),
                    cls="selector-card",
                ),
                cls="index-container",
            )
        ),
    )


@rt("/employee")
def get_employee(id: int = 1):
    content = employee_page(id, employee_model)
    return Html(Head(Title(f"Employee: {employee_model.username(id)}"), *css_headers), Body(content))


@rt("/team")
def get_team(id: int = 1):
    content = team_page(id, team_model)
    return Html(Head(Title(f"Team: {team_model.username(id)}"), *css_headers), Body(content))


if __name__ == "__main__":
    serve()
