from neo4j import GraphDatabase


class Neo4jConnector:
    """
    Initialize Neo4j connection

    Parameters:
        uri (str): Neo4j database URI (e.g., "bolt://localhost:7687")
        user (str): Database username
        password (str): Database password
    """

    def __init__(self, uri, username, password):
        with GraphDatabase.driver(uri, auth=(username, password)) as driver:
            driver.verify_connectivity()
            self.driver = driver

    def close(self):
        """Close the driver connection"""
        self.driver.close()

    def execute_query(self, query, parameters=None):
        """
        Execute a Cypher query

        Parameters:
            query (str): Cypher query to execute
            parameters (dict): Query parameters (optional)
        """
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return list(result)
