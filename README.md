# Alihans-project
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Personal Profile</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<div class="app">

    <!-- LEFT SIDEBAR -->
    <aside class="sidebar">
        <h3>Profile</h3>
        <ul>
            <li>Profile</li>
            <li>Hobbies</li>
            <li>Dreams</li>
            <li>Favorites</li>
            <li>Settings</li>
        </ul>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="content">

        <input class="search" type="text" placeholder="Search memories or dreams…">

        <section class="glass">
            <h1>{{ profile.name }}</h1>
            <p>{{ profile.description }}</p>

            <div class="tags">
                {% for tag in profile.tags %}
                    <span>{{ tag }}</span>
                {% endfor %}
            </div>
        </section>

        <section class="glass">
            <h2>Future Dreams</h2>
            <div class="cards">
                {% for dream in profile.dreams %}
                <div class="card">
                    <img src="{{ dream.image }}" alt="{{ dream.title }}">
                    <p>{{ dream.title }}</p>
                </div>
                {% endfor %}
            </div>
        </section>

    </main>

</div>

</body>
</html>
