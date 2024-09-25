from py2neo import Graph

try:
    graph = Graph("url", auth=("neo4j", "password"))
    result = graph.run("RETURN 'Connection Successful!' AS message")
    print(result.data())  # Should return "Connection Successful!"
except Exception as e:
    print("Connection failed:", e)
