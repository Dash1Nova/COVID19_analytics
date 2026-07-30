import plotly.express as px
import pandas as pd


def create_country_metrics_chart(data):
    df = pd.DataFrame(
        {
            "Metric":
            [
                "Confirmed",
                "Deaths",
                "Recovered",
                "Active"
            ],

            "Value":
            [
                data["confirmed"],
                data["deaths"],
                data["recovered"],
                data["active"]
            ]
        }
    )


    fig = px.bar(
        df,
        x="Metric",
        y="Value",
        title="COVID Metrics"
    )
    return fig



def create_rate_chart(data):
    df = pd.DataFrame(
        {
            "Metric":
            [
                "Mortality",
                "Recovery",
                "Active"
            ],

            "Percentage":
            [
                data["mortality_rate"],
                data["recovery_rate"],
                data["active_rate"]
            ]
        }
    )


    fig = px.pie(
        df,
        names="Metric",
        values="Percentage",
        title="COVID Outcome Rates"
    )
    return fig


def create_comparison_chart(data):
    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="country",
        y="confirmed",
        title="Country Comparison"
    )
    return fig