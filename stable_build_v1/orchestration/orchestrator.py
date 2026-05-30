from engines.doorman import Doorman

from engines.memory_integration import (
    MemoryIntegration
)

from engines.domain_router import (
    DomainRouter
)

from engines.intent_orchestrator import (
    IntentOrchestrator
)

from engines.context_resonance import (
    ContextResonance
)

from engines.conversation_momentum import (
    ConversationMomentum
)

from engines.continuity_weighting import (
    ContinuityWeighting
)

from engines.amplifier import Amplifier

from engines.gatekeeper import Gatekeeper

from engines.understanding_alignment import (
    UnderstandingAlignment
)

from engines.meaning_builder import (
    MeaningBuilder
)

from engines.reasoning_adapter import (
    ReasoningAdapter
)

from engines.depth_gate import (
    DepthGate
)

from engines.stabilization_monitor import (
    StabilizationMonitor
)

from engines.llm_bridge import (
    LLMBridge
)

from engines.voice import (
    Voice
)

from engines.sequence_designer import (
    SequenceDesigner
)

from engines.manifestation_arbiter import (
    ManifestationArbiter
)

from engines.rhythm_balancer import (
    RhythmBalancer
)

from engines.reflective_monitor import (
    ReflectiveMonitor
)

from memory.cognitive_memory import (
    CognitiveMemory
)


class Orchestrator:

    def __init__(self):

        self.memory = (
            CognitiveMemory()
        )

        self.executive_cognition = {

            "priority_mode":
                "balanced",

            "depth_preference":
                "high",

            "stability_enforcement":
                True,

            "semantic_divergence":
                True,

            "presence_identity":
                True,

            "contextual_variability":
                True
        }

        self.cognition_pipeline = [

            Doorman(),

            MemoryIntegration(),

            DomainRouter(),

            IntentOrchestrator(),

            ContextResonance(),

            ConversationMomentum(),

            ContinuityWeighting(),

            Amplifier(),

            Gatekeeper(),

            UnderstandingAlignment(),

            MeaningBuilder(),

            ReasoningAdapter(),

            DepthGate(),

            StabilizationMonitor()
        ]

        self.manifestation_pipeline = [

            LLMBridge(),

            Voice(),

            SequenceDesigner(),

            ManifestationArbiter(),

            RhythmBalancer(),

            ReflectiveMonitor()
        ]

    def run_pipeline(
        self,
        pipeline,
        message_object
    ):

        for engine in pipeline:

            if hasattr(
                engine,
                "protected_process"
            ):

                message_object = (
                    engine.protected_process(
                        message_object
                    )
                )

            else:

                message_object = (
                    engine.process(
                        message_object
                    )
                )

        return message_object

    def executive_arbitration(
        self,
        message_object
    ):

        message_object.cognitive_state[
            "executive_cognition"
        ] = {

            "priority_mode":
                self.executive_cognition[
                    "priority_mode"
                ],

            "depth_preference":
                self.executive_cognition[
                    "depth_preference"
                ],

            "stability_enforcement":
                self.executive_cognition[
                    "stability_enforcement"
                ],

            "semantic_divergence":
                self.executive_cognition[
                    "semantic_divergence"
                ],

            "presence_identity":
                self.executive_cognition[
                    "presence_identity"
                ],

            "contextual_variability":
                self.executive_cognition[
                    "contextual_variability"
                ]
        }

        message_object.enrichment_layers.append({

            "engine":
                "executive_cognition",

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "executive_arbitration",

            "content": {

                "executive_layer_active":
                    True,

                "executive_state":
                    self.executive_cognition
            }
        })

        return message_object

    def store_reflection_memory(
        self,
        message_object
    ):

        reflection_notes = []

        for layer in (
            message_object.enrichment_layers
        ):

            if (
                layer["engine"]
                == "reflective_monitor"
            ):

                reflection_notes = (
                    layer["content"][
                        "reflection_notes"
                    ]
                )

        self.memory.store_reflection(

            message_object.raw_message,

            message_object.final_response,

            reflection_notes
        )

    def structural_response_check(
        self,
        message_object
    ):

        response = (
            message_object.final_response
            .strip()
        )

        if not response:

            return False

        minimum_word_threshold = 40

        response_word_count = len(
            response.split()
        )

        repetitive_fragments = [

            "That pressure tends to accumulate gradually.",

            "Over time, these pressures reshape decision-making.",

            "This tends to influence behavior more than expected."
        ]

        repetitive_count = 0

        for fragment in repetitive_fragments:

            repetitive_count += (
                response.count(fragment)
            )

        if repetitive_count > 2:

            return False

        if response_word_count < minimum_word_threshold:

            return False

        return True

    def run(
        self,
        message_object
    ):

        recursion_state = (
            message_object.recursion_state
        )

        message_object = (
            self.executive_arbitration(
                message_object
            )
        )

        message_object = (
            self.run_pipeline(
                self.cognition_pipeline,
                message_object
            )
        )

        while (

            recursion_state[
                "recursive_thinking_required"
            ]
        ):

            if (

                recursion_state[
                    "loop_count"
                ]

                >= recursion_state[
                    "max_loops"
                ]
            ):

                recursion_state[
                    "recursive_thinking_required"
                ] = False

                break

            recursion_state[
                "loop_count"
            ] += 1

            recursion_state[
                "depth"
            ] += 1

            recursion_state[
                "current_wave"
            ] += 1

            message_object = (
                self.executive_arbitration(
                    message_object
                )
            )

            message_object = (
                self.run_pipeline(
                    self.cognition_pipeline,
                    message_object
                )
            )

            if not recursion_state.get(
                "recursive_thinking_required",
                False
            ):

                break

        recursion_state[
            "recursive_thinking_required"
        ] = False

        message_object = (
            self.run_pipeline(
                self.manifestation_pipeline,
                message_object
            )
        )

        structure_valid = (
            self.structural_response_check(
                message_object
            )
        )

        if not structure_valid:

            message_object.final_response = (

                "I need to reorganize the response structure before answering clearly."
            )

        self.store_reflection_memory(
            message_object
        )

        return message_object
