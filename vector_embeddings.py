# coding: utf-8

# embed_text_demo.py
# Supports Python 3
# Vp(}Y_4k}eQd2:xxbyZd
#ocid1.generativeaihostedapplication.oc1.iad.amaaaaaahvxmx3aau3hd6brvi7kjuivx2ntiywupvxnzqkbp4kb3zvdalaiq
import oci

# ============================================================
# 1. OCI Authentication Configuration
# ============================================================

compartment_id = "ocid1.tenancy.oc1..aaaaaaaac5numqkdcafs7grxz6jnltky2ws3334w4gl2ro7cade6srwelbqq"

CONFIG_PROFILE = "DEFAULT"

config = oci.config.from_file(
    r"C:\Users\jingkhai\Downloads\august-code\config",
    CONFIG_PROFILE
)


# ============================================================
# 2. Generative AI Service Endpoint
# ============================================================

endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"

generative_ai_inference_client = (
    oci.generative_ai_inference.GenerativeAiInferenceClient(
        config=config,
        service_endpoint=endpoint,
        retry_strategy=oci.retry.NoneRetryStrategy(),
        timeout=(10, 240)
    )
)


# ============================================================
# 3. Texts to Embed
# ============================================================

inputs = [
    "hello",
    "underwear",
    "challenge",
    "reading",
    "keyboard"
]


# ============================================================
# 4. Create Embedding Request
# ============================================================

embed_text_detail = (
    oci.generative_ai_inference.models.EmbedTextDetails()
)

embed_text_detail.serving_mode = (
    oci.generative_ai_inference.models.OnDemandServingMode(
        model_id="cohere.embed-english-light-v3.0"
    )
)

embed_text_detail.inputs = inputs

embed_text_detail.truncate = "NONE"

embed_text_detail.compartment_id = compartment_id


# ============================================================
# 5. Call OCI Generative AI Embedding API
# ============================================================

embed_text_response = (
    generative_ai_inference_client.embed_text(
        embed_text_detail
    )
)


# ============================================================
# 6. Print Results
# ============================================================

print("************************* Embed Texts Result *************************")

# print(embed_text_response.data)
print("Number of embeddings:", len(embed_text_response.data.embeddings))

for i, embedding in enumerate(embed_text_response.data.embeddings):
    print(f"\nInput {i + 1}: {inputs[i]}")
    print("Vector dimensions:", len(embedding))
    print("First 10 values:", embedding[:10])