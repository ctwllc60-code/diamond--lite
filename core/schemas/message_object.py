import copy


class MessageObject:

    def __init__(
        self,
        raw_message,
        developer_mode=True
    ):

        self.raw_message = (
            raw_message
        )

        self.developer_mode = (
            developer_mode
        )

        self.enrichment_layers = []

        self.cognitive_state = {}

        self.emotional_state = {}

        self.salience_map = {}

        self.recursion_state = {

            "depth":
                0,

            "revisits":
                [],

            "recursive_thinking_required":
                False,

            "recursive_trigger_engine":
                None,

            "loop_count":
                0,

            "max_loops":
                3,

            "current_wave":
                0
        }

        self.final_response = None

        self.state_snapshots = []

        self.rollback_events = []

    def create_state_snapshot(
        self,
        engine_name
    ):

        snapshot = {

            "engine":
                engine_name,

            "cognitive_state":
                copy.deepcopy(
                    self.cognitive_state
                ),

            "emotional_state":
                copy.deepcopy(
                    self.emotional_state
                ),

            "salience_map":
                copy.deepcopy(
                    self.salience_map
                ),

            "recursion_state":
                copy.deepcopy(
                    self.recursion_state
                ),

            "final_response":
                self.final_response
        }

        self.state_snapshots.append(
            snapshot
        )

    def restore_last_snapshot(
        self
    ):

        if not self.state_snapshots:

            return False

        latest_snapshot = (
            self.state_snapshots[-1]
        )

        self.cognitive_state = (
            copy.deepcopy(
                latest_snapshot[
                    "cognitive_state"
                ]
            )
        )

        self.emotional_state = (
            copy.deepcopy(
                latest_snapshot[
                    "emotional_state"
                ]
            )
        )

        self.salience_map = (
            copy.deepcopy(
                latest_snapshot[
                    "salience_map"
                ]
            )
        )

        self.recursion_state = (
            copy.deepcopy(
                latest_snapshot[
                    "recursion_state"
                ]
            )
        )

        self.final_response = (
            latest_snapshot[
                "final_response"
            ]
        )

        rollback_event = {

            "restored_from_engine":
                latest_snapshot[
                    "engine"
                ],

            "rollback_completed":
                True
        }

        self.rollback_events.append(
            rollback_event
        )

        return True
