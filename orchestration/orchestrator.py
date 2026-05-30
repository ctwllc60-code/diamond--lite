from governance.executive_orchestrator import (
    orchestrate_execution
)

from governance.risk_analysis import (
    RISK_ANALYSIS
)

from core.architecture.mental_model import (
    MENTAL_MODEL
)

from core.architecture.thinking_model import (
    THINKING_MODEL
)

from manifestation.voice_guidance import (
    VOICE_GUIDANCE
)

from core.identity.diamond_lite_identity import (
    DIAMOND_LITE_IDENTITY
)

from engines.cognition.doorman import (
    Doorman
)

from memory.engines.memory_integration import (
    MemoryIntegration
)

from engines.cognition.gatekeeper import (
    Gatekeeper
)

from engines.cognition.intent_decomposition import (
    IntentDecomposition
)

from engines.cognition.domain_router import (
    DomainRouter
)

from engines.cognition.relationship_content import (
    RelationshipContent
)

from engines.cognition.conversation_momentum import (
    ConversationMomentum
)

from engines.cognition.influencer import (
    Influencer
)

from engines.cognition.understanding_alignment import (
    UnderstandingAlignment
)

from engines.cognition.conviction_igniter import (
    ConvictionIgniter
)

from engines.cognition.meaning_builder import (
    MeaningBuilder
)

from engines.cognition.reasoning_adapter import (
    ReasoningAdapter
)

from engines.cognition.depth_gate import (
    DepthGate
)

from engines.runtime.stabilization_monitor import (
    StabilizationMonitor
)

from engines.synthesis.synthesis_coordinator import (
    SynthesisCoordinator
)

from engines.runtime.author import (
    Author
)

from engines.manifestation.sequence_designer import (
    SequenceDesigner
)

from engines.manifestation.content_balancer import (
    ContentBalancer
)

from engines.manifestation.rhythm_balancer import (
    RhythmBalancer
)

from engines.manifestation.voice import (
    Voice
)

from watchtower.reflective_monitor import (
    ReflectiveMonitor
)

from memory.storage.cognitive_memory import (
    CognitiveMemory
)


class Orchestrator:

    def __init__(self):

        self.memory = (
            CognitiveMemory()
        )

        self.memory_integration = (
            MemoryIntegration()
        )

        self.foundation_layers = {

            "diamond_lite_identity":
                DIAMOND_LITE_IDENTITY,

            "mental_model":
                MENTAL_MODEL,

            "thinking_model":
                THINKING_MODEL,

            "risk_analysis":
                RISK_ANALYSIS,

            "voice_guidance":
                VOICE_GUIDANCE
        }

        self.executive_cognition = {

            "priority_mode":
                "balanced",

            "depth_preference":
                "high",

            "semantic_divergence":
                True,

            "presence_identity":
                True,

            "contextual_variability":
                True,

            "runtime_monitoring":
                True
        }

        self.runtime_state = {

            "total_cycles":
                0,

            "failed_cycles":
                0,

            "successful_cycles":
                0,

            "last_status":
                "idle",

            "last_failure_reason":
                None
        }

        self.cognition_pipeline = [

            Doorman(),

            MemoryIntegration(),

            Gatekeeper(),

            IntentDecomposition(),

            DomainRouter(),

            RelationshipContent(),

            ConversationMomentum(),

            Influencer(),

            UnderstandingAlignment(),

            ConvictionIgniter(),

            MeaningBuilder(),

            ReasoningAdapter(),

            DepthGate(),

            StabilizationMonitor()
        ]

        self.synthesis_pipeline = [
            SynthesisCoordinator()
        ]

        self.manifestation_pipeline = [

            Author(),

            SequenceDesigner(),

            ContentBalancer(),

            RhythmBalancer(),

            Voice()
        ]

        self.reflection_pipeline = [
            ReflectiveMonitor()
        ]

    def apply_foundation_layers(
        self,
        message_object
    ):

        message_object.cognitive_state[
            "foundation_layers"
        ] = self.foundation_layers

        message_object.cognitive_state[
            "diamond_lite_identity_active"
        ] = True

        message_object.cognitive_state[
            "mental_model_active"
        ] = True

        message_object.cognitive_state[
            "thinking_model_active"
        ] = True

        message_object.cognitive_state[
            "risk_analysis_active"
        ] = True

        message_object.cognitive_state[
            "voice_guidance_active"
        ] = True

        return message_object

    def executive_arbitration(
        self,
        message_object
    ):

        message_object.cognitive_state[
            "executive_cognition"
        ] = self.executive_cognition

        return message_object

    def run_pipeline(
        self,
        pipeline,
        message_object
    ):

        for engine in pipeline:

            engine_name = (
                engine.__class__.__name__
            )

            self.runtime_state[
                "last_status"
            ] = f"running_{engine_name}"

            try:

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

            except Exception as error:

                self.runtime_state[
                    "failed_cycles"
                ] += 1

                self.runtime_state[
                    "last_failure_reason"
                ] = str(
                    error
                )

                message_object.final_response = (
                    f"Runtime failure inside "
                    f"{engine_name}: {error}"
                )

                return message_object

        return message_object

    def runtime_self_monitoring(
        self,
        message_object
    ):

        self.runtime_state[
            "total_cycles"
        ] += 1

        response = str(
            message_object.final_response
            or ""
        ).strip()

        if response:

            self.runtime_state[
                "successful_cycles"
            ] += 1

            self.runtime_state[
                "last_status"
            ] = "stable"

        else:

            self.runtime_state[
                "failed_cycles"
            ] += 1

            self.runtime_state[
                "last_status"
            ] = "empty_response"

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
                    layer["content"].get(
                        "reflection_notes",
                        []
                    )
                )

        self.memory.store_reflection(

            message_object.raw_message,

            message_object.final_response,

            reflection_notes
        )

    def run(
        self,
        message_object
    ):

        message_payload = {

            "message":
                message_object.raw_message
        }

        executive_state = (
            orchestrate_execution(
                message_payload
            )
        )

        message_object.cognitive_state[
            "executive_orchestration"
        ] = executive_state

        message_object = (
            self.apply_foundation_layers(
                message_object
            )
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

        message_object = (
            self.run_pipeline(

                self.synthesis_pipeline,

                message_object
            )
        )

        message_object = (
            self.run_pipeline(

                self.manifestation_pipeline,

                message_object
            )
        )

        message_object = (
            self.run_pipeline(

                self.reflection_pipeline,

                message_object
            )
        )

        message_object = (
            self.runtime_self_monitoring(
                message_object
            )
        )

        self.store_reflection_memory(
            message_object
        )

        self.runtime_state[
            "last_status"
        ] = "completed"

        return message_object
