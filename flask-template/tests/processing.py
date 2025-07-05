def process_data(data):
    # Example processing logic
    popular_routes = {}
    for entry in data:
        route = entry['route']
        price = float(entry['price'].replace('$', ''))
        if route not in popular_routes:
            popular_routes[route] = {'count': 0, 'total_price': 0}
        popular_routes[route]['count'] += 1
        popular_routes[route]['total_price'] += price

    for route, info in popular_routes.items():
        info['average_price'] = info['total_price'] / info['count']

    return popular_routes
