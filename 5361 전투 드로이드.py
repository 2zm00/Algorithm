def calculate_cost():
    prices = {
        'blaster_rifle': 350.34,
        'visual_sensor': 230.90,
        'audio_sensor': 190.55,
        'arm': 125.30,
        'leg': 180.90
    }

    num_test_cases = int(input())

    for _ in range(num_test_cases):
        A, B, C, D, E = map(int, input().split())

        total_cost = (
            A * prices['blaster_rifle'] +
            B * prices['visual_sensor'] +
            C * prices['audio_sensor'] +
            D * prices['arm'] +
            E * prices['leg']
        )

        print(f"${total_cost:.2f}")

calculate_cost()
