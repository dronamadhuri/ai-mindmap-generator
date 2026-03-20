def generate_mindmap(data):
    nodes = []
    links = []

    main = data["main_topic"]
    nodes.append({"id": main, "group": 1})

    for category in data["categories"]:
        cat = category["name"]
        nodes.append({"id": cat, "group": 2})
        links.append({"source": main, "target": cat})

        for sub in category["subtopics"]:
            sub_name = sub["name"]
            nodes.append({"id": sub_name, "group": 3})
            links.append({"source": cat, "target": sub_name})

            for point in sub["points"]:
                nodes.append({"id": point, "group": 4})
                links.append({"source": sub_name, "target": point})

    return {"nodes": nodes, "links": links}