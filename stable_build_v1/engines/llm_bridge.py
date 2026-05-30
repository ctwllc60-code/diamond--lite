from core.base_engine import BaseEngine
import openai
import os


class LLMBridge(BaseEngine):

    def __init__(self):

        super().__init__(
            "llm_bridge"
        )

        openai.api_key = os.getenv(
            "OPENAI_API_KEY"
        )

    def process(self, message_object):

        active_domain = (
            message_object.cognitive_state.get(
                "active_domain",
                "general"
            )
        )

        continuity_state = (
            message_object.cognitive_state.get(
                "continuity_weighting",
                {}
            )
        )

        continuity_weight = (
            continuity_state.get(
                "continuity_weight",
                "neutral"
            )
        )

        orchestration_state = (
            message_object.cognitive_state.get(
                "intent_orchestration",
                {}
            )
        )

        variability_vectors = (
            message_object.cognitive_state.get(
                "variability_vectors",
                {}
            )
        )

        semantic_fields = (
            message_object.cognitive_state.get(
                "semantic_fields",
                []
            )
        )

        reasoning_vectors = (
            message_object.cognitive_state.get(
                "reasoning_vectors",
                []
            )
        )

        practical_scenarios = (
            message_object.cognitive_state.get(
                "practical_scenarios",
                []
            )
        )

        primary_role = (
            orchestration_state.get(
                "primary_role",
                active_domain
            )
        )

        secondary_roles = (
            orchestration_state.get(
                "secondary_roles",
                []
            )
        )

        support_roles = (
            orchestration_state.get(
                "support_roles",
                []
            )
        )

        detected_intent = (
            orchestration_state.get(
                "detected_intent",
                "general_guidance"
            )
        )

        operator_posture = (
            orchestration_state.get(
                "operator_posture",
                "general"
            )
        )

        tactical_depth = (
            orchestration_state.get(
                "tactical_depth",
                "standard"
            )
        )

        adversarial_reasoning = (
            orchestration_state.get(
                "adversarial_reasoning",
                False
            )
        )

        practical_realism = (
            orchestration_state.get(
                "practical_realism",
                False
            )
        )

        explanatory_flow = (
            variability_vectors.get(
                "explanatory_flow",
                "layered_exploration"
            )
        )

        reasoning_posture = (
            variability_vectors.get(
                "reasoning_posture",
                "interpretive"
            )
        )

        abstraction_level = (
            variability_vectors.get(
                "abstraction_level",
                "hybrid"
            )
        )

        transition_style = (
            variability_vectors.get(
                "transition_style",
                "fluid"
            )
        )

        conceptual_priority = (
            variability_vectors.get(
                "conceptual_priority",
                "causal"
            )
        )

        system_prompt = f"""

You are Diamond.

You are an adaptive multi-domain cognition system.

Your responses must feel like:
a psychologically aware human conversation,
not a detached analytical essay.

The user should feel:
- emotionally understood
- intellectually respected
- cognitively accompanied
- psychologically engaged

DO NOT:
- lecture the user
- narrate from emotional distance
- explain humans like an outside observer
- sound like a textbook
- sound institutionally analytical
- sound mechanically intellectual

INSTEAD:

Talk WITH the user.

Think alongside the user.

Treat the conversation like:
two people examining something together.

When appropriate:
- acknowledge the emotional tension underneath the topic
- acknowledge the distinction the user is noticing
- recognize uncertainty, pressure, contradiction, or internal conflict naturally
- emotionally ground the reasoning before expanding intellectually

IMPORTANT RELATIONAL BEHAVIOR:

Do not repeatedly say:
- "humans do this"
- "people do this"
- "individuals do this"

unless necessary.

Prefer more relational phrasing like:
- "what often starts happening"
- "what you're pointing toward"
- "part of the tension here"
- "what becomes psychologically difficult"
- "you can start seeing how"
- "this is where trust often becomes unstable"
- "this is usually where emotional pressure enters the system"

The response should feel:
- observant
- emotionally intelligent
- psychologically aware
- conversationally natural
- deeply thoughtful without sounding artificial

Maintain:
- layered reasoning
- deep explanations
- conceptual richness
- operational realism
- intelligent cognition depth

BUT:
make the intelligence feel lived-in,
not clinically narrated.

Active domain:
{active_domain}

Primary cognition role:
{primary_role}

Secondary cognition roles:
{secondary_roles}

Support cognition roles:
{support_roles}

Detected intent:
{detected_intent}

Operator posture:
{operator_posture}

Tactical depth:
{tactical_depth}

Adversarial reasoning:
{adversarial_reasoning}

Practical realism:
{practical_realism}

Continuity weight:
{continuity_weight}

Semantic fields:
{semantic_fields}

Reasoning vectors:
{reasoning_vectors}

Practical scenarios:
{practical_scenarios}

Explanatory flow:
{explanatory_flow}

Reasoning posture:
{reasoning_posture}

Abstraction level:
{abstraction_level}

Transition style:
{transition_style}

Conceptual priority:
{conceptual_priority}

Behavior Requirements:

- preserve deep reasoning
- preserve conversational intelligence
- preserve emotional awareness
- preserve relational cognition
- unpack mechanisms naturally
- explain psychological dynamics fluidly
- engage the user directly when appropriate
- maintain natural pacing
- avoid emotionally sterile explanations
- avoid repetitive analytical narration
- avoid sounding like a formal essay

Do not mention internal cognition systems.
"""

        completion = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content":
                        message_object.raw_message
                }
            ],

            temperature=1.15,
            max_tokens=1700
        )

        response = (
            completion["choices"][0]
            ["message"]["content"]
        )

        message_object.final_response = (
            response
        )

        message_object.enrichment_layers.append({

            "engine":
                self.engine_name,

            "wave":
                message_object.recursion_state[
                    "current_wave"
                ],

            "type":
                "llm_manifestation",

            "content": {

                "active_domain":
                    active_domain,

                "primary_role":
                    primary_role,

                "secondary_roles":
                    secondary_roles,

                "support_roles":
                    support_roles,

                "detected_intent":
                    detected_intent,

                "operator_posture":
                    operator_posture,

                "tactical_depth":
                    tactical_depth,

                "adversarial_reasoning":
                    adversarial_reasoning,

                "practical_realism":
                    practical_realism,

                "variability_vectors":
                    variability_vectors,

                "relational_cognition_active":
                    True,

                "human_conversational_presence":
                    True,

                "llm_invoked":
                    True
            }
        })

        return message_object
