"""
Centralized configuration for the GIG project.
"""

# Database paths
DB_PATH = "data/ideas.db"
BLOCKCHAIN_DB_PATH = "data/blockchain.db"
TEMPORAL_DB_PATH = "data/temporal_memory.db"

# LLM Configuration
OLLAMA_MODEL = "llama3.2:1b"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Ranking weights
ALPHA_WEIGHTS = {
    "elo": 0.15,
    "bayesian": 0.20,
    "uncertainty": 0.10,
    "sentiment": 0.12,
    "provenance": 0.08,
    "freshness": 0.10,
    "trend": 0.10,
    "causal": 0.10,
    "serendipity": 0.05,
}

# Other parameters
TIME_DECAY_LAMBDA = 0.01
ELO_K_FACTOR = 32
BAYESIAN_PRIOR_MEAN = 0.5
BAYESIAN_PRIOR_STD = 0.3
CAUSAL_THRESHOLD = 0.3
FEASIBILITY_WEIGHTS = {
    "market_size": 0.3,
    "revenue": 0.3,
    "cost": 0.2,
    "trend": 0.1,
    "sentiment": 0.1,
}
FEDERATED_PRIVACY_EPSILON = 1.0
FEDERATED_AGGREGATION = "fedavg"
TEMPORAL_TTL_HOURS = 168
BLOCKCHAIN_DIFFICULTY = 1
ETHICS_PROHIBITED_KEYWORDS = [
    "violence", "fraud", "discrimination", "illegal"
]
ETHICS_HIGH_RISK_DOMAINS = [
    "gambling", "weapons", "adult content"
]
EVALUATION_K_VALUES = [1, 3, 5, 10]
CROSS_VALIDATION_FOLDS = 5
TOP_K_RECOMMENDATIONS = 5
NUM_IDEAS_TO_GENERATE = 3
DEFAULT_PROMPT = "sustainable technology for climate change"
AQI_PROMPT = "give me hardware based idea for me to control aqi of delhi"
