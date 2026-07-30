from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px

from api_client import (
    get_summary,
    get_country_analytics,
    compare_countries,
    get_comments,
    add_comment
)

from charts import (
    create_country_metrics_chart,
    create_rate_chart,
    create_comparison_chart
)

app = Dash(__name__)

countries = [
    "Lithuania",
    "Latvia",
    "Estonia",
    "Germany",
    "France",
    "USA"
]


app.layout = html.Div(
    [
        html.H1(
            "COVID-19 Analytics Dashboard"
        ),

        html.Hr(),

        html.H2(
            "Global Summary"
        ),

        html.Div(
            id="summary"
        ),

        html.Hr(),

        html.H2(
            "Country Analysis"
        ),

        dcc.Dropdown(
            countries,
            value="Lithuania",
            id="country-dropdown"
        ),

        dcc.Graph(
            id="metrics-chart"
        ),

        dcc.Graph(
            id="rate-chart"
        ),

        html.Hr(),

        html.H2(
            "Country Comparison"
        ),

        dcc.Dropdown(
            countries,
            value="Lithuania",
            id="country1"
        ),

        dcc.Dropdown(
            countries,
            value="Latvia",
            id="country2"
        ),

        dcc.Graph(
            id="comparison-chart"
        ),

        html.Hr(),

        html.H2(
            "Analyst Comments"
        ),

        dcc.Dropdown(
            countries,
            value="Lithuania",
            id="comment-country"
        ),

        dcc.Textarea(
            id="comment-text",
            placeholder="Write comment..."
        ),

        html.Button(
            "Add Comment",
            id="add-comment"
        ),

        html.Div(
            id="comments"
        )
    ]
)


@app.callback(
    Output(
        "summary",
        "children"
    ),

    Input(
        "country-dropdown",
        "value"
    )
)

def update_summary(_):
    data = get_summary()
    return html.Div(
        [

            html.P(
                f"Countries: {data['countries']}"
            ),

            html.P(
                f"Confirmed: {data['confirmed']}"
            ),

            html.P(
                f"Deaths: {data['deaths']}"
            ),

            html.P(
                f"Recovered: {data['recovered']}"
            )
        ]
    )


@app.callback(
    Output(
        "metrics-chart",
        "figure"
    ),

    Output(
        "rate-chart",
        "figure"
    ),

    Input(
        "country-dropdown",
        "value"
    )
)

def update_country(country):
    data = get_country_analytics(
        country
    )
    return (
        create_country_metrics_chart(data),
        create_rate_chart(data)
    )


@app.callback(
    Output(
        "comparison-chart",
        "figure"
    ),


    Input(
        "country1",
        "value"
    ),

    Input(
        "country2",
        "value"
    )
)

def update_compare(
    country1,
    country2
):
    data = compare_countries(
        country1,
        country2
    )
    return create_comparison_chart(data)


@app.callback(
    Output(
        "comments",
        "children"
    ),

    Input(
        "comment-country",
        "value"
    )
)

def show_comments(country):
    comments = get_comments(country)
    return [
        html.P(
            c["comment"]
        )
        for c in comments
    ]


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8050
    )