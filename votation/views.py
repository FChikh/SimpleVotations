from django.shortcuts import render


def main(request):
    data = {}
    data["votes"] = [
        [
            {
                "title": "Собачки",
                "percentage": 10
            },
            {
                "title": "Котики",
                "percentage": 20
            },
            {
                "title": "Единая Россия",
                "percentage": 70
            }
        ]
    ]
    # Хардкод
    data["votes"] *= 10
    return render(request, "main.html", data)


def profile(request):
    data = {}
    data['name'] = "Игорь"
    data['surname'] = "Нуруллаев"
    data["votes_history"] = [
        [
            {
                "title": "Собачки",
                "percentage": 10
            },
            {
                "title": "Котики",
                "percentage": 20
            },
            {
                "title": "Единая Россия",
                "percentage": 70
            }
        ]
    ]
    # Хардкод
    data["votes_history"] *= 10
    return render(request, "profile.html", data)
