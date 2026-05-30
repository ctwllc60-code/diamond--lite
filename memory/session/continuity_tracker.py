class ContinuityTracker:

    def __init__(self):

        self.active_topics = []

    def register_topic(
        self,
        topic
    ):

        if (
            topic
            not in self.active_topics
        ):

            self.active_topics.append(
                topic
            )

        self.active_topics = (
            self.active_topics[-25:]
        )

    def retrieve_topics(
        self
    ):

        return self.active_topics
