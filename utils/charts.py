import plotly.express as px


def priority_chart(df):

    fig = px.pie(
        df,
        names="Priority",
        title="Task Priority Distribution"
    )

    return fig


def status_chart(df):

    fig = px.bar(
        df,
        x="Status",
        title="Task Status"
    )

    return fig


def subject_chart(df):

    fig = px.histogram(
        df,
        x="Subject",
        title="Tasks per Subject"
    )

    return fig