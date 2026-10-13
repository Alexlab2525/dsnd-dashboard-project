from .sql_execution import QueryMixin


class QueryBase(QueryMixin):
    """Base class for Employee and Team. Holds shared SQL queries."""

    name: str = ""

    def names(self) -> list:
        raise NotImplementedError

    def username(self, id: int) -> str:
        raise NotImplementedError

    def model_data(self, id: int):
        raise NotImplementedError

    def event_counts(self, id: int):
        sql = f"""
            SELECT
                event_date,
                SUM(positive_events) AS positive_events,
                SUM(negative_events) AS negative_events
            FROM   employee_events
            WHERE  {self.name}_id = {id}
            GROUP  BY event_date
            ORDER  BY event_date
        """
        return self.pandas_query(sql)

    def notes(self, id: int):
        sql = f"""
            SELECT note_date, note
            FROM   notes
            WHERE  {self.name}_id = {id}
            ORDER  BY note_date DESC
        """
        return self.pandas_query(sql)
