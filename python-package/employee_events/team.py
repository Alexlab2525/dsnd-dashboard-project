from .query_base import QueryBase


class Team(QueryBase):
    """SQL queries scoped to an entire team."""

    name = "team"

    def names(self) -> list:
        sql = """
            SELECT team_id, team_name
            FROM   team
            ORDER  BY team_name
        """
        return self.tuple_query(sql)

    def username(self, id: int) -> str:
        sql = f"""
            SELECT team_name
            FROM   team
            WHERE  team_id = {id}
        """
        result = self.tuple_query(sql)
        return result[0][0] if result else "Unknown Team"

    def model_data(self, id: int):
        sql = f"""
            SELECT employee_id,
                   SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM   employee_events
            WHERE  team_id = {id}
            GROUP  BY employee_id
        """
        return self.pandas_query(sql)
