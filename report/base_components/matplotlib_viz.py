import io, base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from fasthtml.common import Img, Div, P
from .base_component import BaseComponent


class MatplotlibViz(BaseComponent):
    """Renders a matplotlib Figure as a base-64 encoded <img>."""

    def component_data(self, entity_id, model):
        return model.event_counts(entity_id)

    def visualization(self, data, entity_id, model):
        fig, ax = plt.subplots(figsize=(10, 4))
        if data is not None and not data.empty:
            x = range(len(data))
            ax.plot(x, data["positive_events"], label="Positive", color="steelblue", marker="o")
            ax.plot(x, data["negative_events"],  label="Negative", color="tomato",    marker="o")
            step = max(1, len(data) // 8)
            ax.set_xticks(list(x)[::step])
            ax.set_xticklabels(data["event_date"].iloc[::step], rotation=45, ha="right", fontsize=8)
            ax.legend(); ax.grid(True, alpha=0.3)
        else:
            ax.text(0.5, 0.5, "No data available", ha="center", va="center", transform=ax.transAxes)
        fig.tight_layout()
        return fig

    @staticmethod
    def fig_to_img_tag(fig):
        buf = io.BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight", dpi=120)
        buf.seek(0)
        encoded = base64.b64encode(buf.read()).decode("utf-8")
        plt.close(fig)
        return Img(src=f"data:image/png;base64,{encoded}", cls="chart", style="max-width:100%;")

    def build_component(self, entity_id, model):
        data = self.component_data(entity_id, model)
        fig  = self.visualization(data, entity_id, model)
        return self.fig_to_img_tag(fig)
