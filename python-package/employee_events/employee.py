from .query_base import QueryBase


class Employee(QueryBase):
    """SQL queries scoped to a single employee."""

    name = "employee"

    def names(self) -> list:
        sql = """
            SELECT employee_id,
                   first_name || ' ' || last_name AS full_name
            FROM   employee
            ORDER  BY last_name, first_name
        """
        return self.tuple_query(sql)

    def username(self, id: int) -> str:
        sql = f"""
            SELECT first_name || ' ' || last_name
            FROM   employee
            WHERE  employee_id = {id}
        """
        result = self.tuple_query(sql)
        return result[0][0] if result else "Unknown Employee"

    def model_data(self, id: int):
        sql = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM   employee_events
            WHERE  employee_id = {id}
        """
        return self.pandas_query(sql)
