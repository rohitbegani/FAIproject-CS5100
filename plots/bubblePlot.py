import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls


class BubblePlot:
    def __init__(self, testData=None, predictions=None, userData=None):
        tls.set_credentials_file(username='bhanujain', api_key='pic17ydt8e')
        self.testData = testData
        self.predictions = predictions
        self.user = userData
        self._businessLatList = []
        self._businessLonList = []
        self._businessRatingList = []
        self._businessTextList = []
        self._predictionRatingList = []
        self._predictionLonList = []
        self._predictionLatList = []
        self._predictionTextList = []

    def initBusiness(self):
        for business in self.testData:
            self._businessLatList.append(business.location_lat)
            self._businessLonList.append(business.location_lon)
            self._businessRatingList.append(business.userRating * 5)
            self._businessTextList.append("Name: %s<br> User Rating: %s<br> General Rating: %s" % (
                business.name, business.userRating, business.stars))

    def initPredictions(self):
        for index, business in enumerate(self.predictions):
            self._predictionLatList.append(business.location_lat)
            self._predictionLonList.append(business.location_lon)
            self._predictionRatingList.append(business.userRating * 5)
            self._predictionTextList.append(
                "Name: %s<br> User Rating: %s<br> General Rating: %s<br> Prediction Rank: %s" % (
                    business.name, business.userRating, business.stars, index+1))

    def generate(self):
        self.initBusiness()
        self.initPredictions()
        trace0 = go.Scatter(
                x=[self.user.location_lat],
                y=[self.user.location_lon],
                mode='markers',
                name='Current User',
                text=["Current User %s" % self.user.location_lat],
                marker=dict(
                        symbol='diamond-dot',
                        sizemode='diameter',
                        sizeref=0.85,
                        size=[self.user.userRating * 5],
                        line=dict(
                                width=2
                        ),
                )
        )

        trace1 = go.Scatter(
                x=self._businessLatList,
                y=self._businessLonList,
                mode='markers',
                name='Business',
                text=self._businessTextList,
                marker=dict(
                        symbol='circle-open',
                        sizemode='diameter',
                        sizeref=0.85,
                        size=self._businessRatingList,
                        line=dict(
                                width=2
                        ),
                )
        )

        trace2 = go.Scatter(
                x=self._predictionLatList,
                y=self._predictionLonList,
                mode='markers',
                name='Predictions',
                text=self._predictionTextList,
                marker=dict(
                        symbol='circle',
                        sizemode='diameter',
                        sizeref=0.85,
                        size=self._predictionRatingList,
                        line=dict(
                                width=2
                        ),
                )
        )

        data = [trace0, trace1, trace2]
        layout = go.Layout(
                title='Location Bases User Prediction',
                xaxis=dict(
                        title='Latitude',
                        gridcolor='rgb(255, 255, 255)',
                        zerolinewidth=1,
                        ticklen=1,
                        gridwidth=.0001,
                        autorange=True,
                ),
                yaxis=dict(
                        title='Longitude',
                        gridcolor='rgb(255, 255, 255)',
                        zerolinewidth=1,
                        ticklen=1,
                        gridwidth=.0001,
                        autorange=True,
                ),
                paper_bgcolor='rgb(243, 243, 243)',
                plot_bgcolor='rgb(243, 243, 243)',
        )
        fig = go.Figure(data=data, layout=layout)
        plot_url = py.plot(fig, filename='location-bases-user-prediction')
