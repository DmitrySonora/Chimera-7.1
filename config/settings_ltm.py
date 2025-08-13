# ========================================
# LONG-TERM MEMORY (LTM)
# ========================================

# LTM Buffer settings - TODO: implement in Next Phases
# LTM_RETENTION_DAYS = 365  # Placeholder - needs complex archival strategy
# WARNING: Simple deletion will break future personality evolution analysis

# LTM Memory types
LTM_MEMORY_TYPES = ['self_related', 'world_model', 'user_related']

# LTM Score constraints
LTM_SCORE_MIN = 0.0
LTM_SCORE_MAX = 1.0

# Коэффициент влияния maturity на порог
LTM_MATURITY_IMPACT_FACTOR = 0.1  # !!! 0.1 = макс +6% к порогу для молодых профилей

# LTM Field lengths
LTM_USER_ID_MAX_LENGTH = 255
LTM_MEMORY_TYPE_MAX_LENGTH = 50
LTM_TRIGGER_REASON_MAX_LENGTH = 100

# LTM Array field limits
LTM_DOMINANT_EMOTIONS_MAX_SIZE = 10
LTM_SEMANTIC_TAGS_MAX_SIZE = 20

# LTM Conversation fragment settings
LTM_CONVERSATION_FRAGMENT_MAX_MESSAGES = 10
LTM_CONVERSATION_FRAGMENT_DEFAULT_WINDOW = 5

# LTM Message content truncation
LTM_MESSAGE_CONTENT_MAX_LENGTH = 2000

# LTM Trigger reasons
LTM_TRIGGER_REASONS = [
    'emotional_peak',
    'emotional_shift', 
    'self_reference',
    'deep_insight',
    'personal_revelation',
    'relationship_change',
    'creative_breakthrough'
]

# LTM Emotional thresholds
LTM_EMOTIONAL_PEAK_THRESHOLD = 0.77
LTM_EMOTIONAL_SHIFT_THRESHOLD = 0.55
LTM_EMOTIONAL_THRESHOLD = 0.4           # !!! Порог для сохранения в LTM, 0.4 - для наблюдения, 0.55- для продакшн (0.6 = ~1-5% сообщений)

# LTM Default values
LTM_DEFAULT_ACCESS_COUNT = 0
LTM_DEFAULT_SELF_RELEVANCE_SCORE = None  # Optional field

# LTM Actor settings
LTM_QUERY_TIMEOUT = 5.0                 # Query timeout in seconds
LTM_METRICS_ENABLED = True              # Enable metrics collection
LTM_METRICS_LOG_INTERVAL = 300          # Metrics logging interval in seconds
LTM_SCHEMA_CHECK_TIMEOUT = 5.0          # Schema verification timeout

# LTM Search settings
LTM_SEARCH_MAX_LIMIT = 100              # Maximum results per search
LTM_SEARCH_DEFAULT_LIMIT = 10           # Default search results limit
LTM_SEARCH_TAGS_MODE_ANY = 'any'        # At least one tag matches
LTM_SEARCH_TAGS_MODE_ALL = 'all'        # All tags must match
LTM_SEARCH_RECENT_DAYS_DEFAULT = 7      # Default days for recent memories
LTM_SEARCH_MIN_IMPORTANCE_DEFAULT = 0.8 # Default min importance score



# ========================================
# LTM NOVELTY ASSESSMENT
# ========================================

LTM_PERCENTILE_ADJUSTMENT_FACTOR = 0.3  # !!! Коэффициент для расчета динамического порога от 90-го перцентиля: 0.3 для отладки, 0.7 для продакшн

# Novelty assessment weights (must sum to 1.0)
LTM_NOVELTY_SEMANTIC_WEIGHT = 0.4      # Weight for semantic distance factor
LTM_NOVELTY_EMOTIONAL_WEIGHT = 0.15    # Weight for emotional rarity factor
LTM_NOVELTY_CONTEXT_WEIGHT = 0.25       # Weight for context rarity factor
LTM_NOVELTY_TEMPORAL_WEIGHT = 0.2     # Weight for temporal novelty factor

# Cold start parameters
LTM_COLD_START_BUFFER_SIZE = 10        # Messages to accumulate before saving
LTM_COLD_START_MIN_THRESHOLD = 0.4     # Minimum novelty threshold
LTM_NOVELTY_SCORES_WINDOW = 90        # Size of recent scores window

# KNN density parameters
LTM_KNN_NEIGHBORS = 7                   # Number of nearest neighbors
LTM_KNN_DENSITY_THRESHOLD = 0.18         # Distance threshold for density
LTM_KNN_DENSITY_PENALTY = 0.25           # Weight reduction for dense regions

# Emotion frequency threshold
LTM_EMOTION_FREQUENCY_THRESHOLD = 0.18   # Min emotion value to count
LTM_PERCENTILE_MIN_SAMPLES = 15        # Min samples for percentile calc

# Maturity sigmoid rate
LTM_MATURITY_SIGMOID_RATE = 0.09        # Rate for sigmoid maturity factor



# ========================================
# LTM EMBEDDINGS
# ========================================

# Модель для генерации embeddings
LTM_EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LTM_EMBEDDING_DEVICE = "cpu"  # или "cuda" при наличии GPU
LTM_EMBEDDING_CACHE_DIR = "./models/cache"

# Размерности композитного embedding (768d total)
LTM_EMBEDDING_SEMANTIC_DIM = 384
LTM_EMBEDDING_EMOTIONAL_DIM = 128  
LTM_EMBEDDING_TEMPORAL_DIM = 64
LTM_EMBEDDING_PERSONAL_DIM = 192

# Параметры векторизации
LTM_EMBEDDING_BATCH_SIZE = 32
LTM_EMBEDDING_MAX_LENGTH = 512
LTM_EMBEDDING_NORMALIZE = True

# Thread pool settings for async embedding generation
LTM_EMBEDDING_THREAD_POOL_SIZE = 2
LTM_EMBEDDING_GENERATION_TIMEOUT = 10.0  # Timeout in seconds (not used yet, reserved for future)

LTM_EMBEDDING_REQUEST_TIMEOUT = 2.0  # Timeout для запроса embedding в секундах
LTM_VECTOR_CACHE_TTL = 3600  # TTL для кэша векторного поиска (1 час)



# ========================================
# LTM ANALYTICS SETTINGS
# ========================================

# Emotional similarity search
LTM_ANALYTICS_SIMILARITY_THRESHOLD = 0.7        # Default cosine similarity threshold
LTM_ANALYTICS_EMOTIONAL_SIMILARITY_LIMIT = 10   # Default limit for similarity search

# Pattern detection
LTM_ANALYTICS_PATTERN_MIN_OCCURRENCES = 3       # Min occurrences to consider a pattern

# Emotional trajectory
LTM_ANALYTICS_TRAJECTORY_DEFAULT_DAYS = 30      # Default time window for trajectories
LTM_ANALYTICS_TRAJECTORY_DEFAULT_GRANULARITY = 'day'  # Default time granularity

# Concept associations
LTM_ANALYTICS_CONCEPT_ASSOCIATIONS_LIMIT = 20   # Max memories to analyze per concept

# Trend detection thresholds
LTM_ANALYTICS_TREND_INCREASE_THRESHOLD = 0.05   # Min avg change for increasing trend
LTM_ANALYTICS_TREND_DECREASE_THRESHOLD = -0.05  # Max avg change for decreasing trend

# Mood search
LTM_ANALYTICS_MOOD_MATCH_THRESHOLD = 0.3        # Min weighted score for mood match

# Importance distribution
LTM_ANALYTICS_HISTOGRAM_BUCKETS = 10            # Number of buckets for importance histogram
LTM_ANALYTICS_ANOMALY_STD_DEVS = 2              # Standard deviations for anomaly detection



# ========================================
# LTM Cache settings
# ========================================

LTM_CACHE_ENABLED = True                # Enable Redis caching for LTM
LTM_CACHE_KEY_PREFIX = "ltm"           # Prefix for all LTM cache keys
LTM_CACHE_DEFAULT_TTL = 1800           # Default TTL in seconds (30 minutes)

# Novelty cache specific settings
LTM_NOVELTY_CACHE_TTL = 1800           # 30 minutes for final results
LTM_NOVELTY_CACHE_LOG_INTERVAL = 100   # Log stats every N requests

# Intermediate computations cache TTL
LTM_EMBEDDING_CACHE_TTL = 3600         # 1 hour - embeddings don't change
LTM_KNN_CACHE_TTL = 900                # 15 minutes - changes with new memories  
LTM_TEMPORAL_CACHE_TTL = 1200          # 20 minutes - changes with new tags

# Profile and state cache TTL
LTM_PROFILE_CACHE_TTL = 21600          # 6 hours - full profile
LTM_PERCENTILE_CACHE_TTL = 3600        # 1 hour - changes with new scores
LTM_CALIBRATION_CACHE_TTL = 7200       # 2 hours - rarely changes after calibration

# Cache metrics and monitoring
LTM_CACHE_METRICS_ENABLED = True        # Enable cache metrics collection
LTM_CACHE_HIT_RATE_ALERT = 0.5         # Alert threshold for low hit rate



# ========================================
# LTM Request settings
# ========================================

LTM_REQUEST_TIMEOUT = 0.5              # Timeout in seconds for LTM response (500ms)
LTM_CONTEXT_LIMIT = 3                  # Maximum number of LTM memories to include in context
LTM_REQUEST_ENABLED = True             # Global switch for LTM integration
LTM_DEFAULT_SEARCH_TYPE = "recent"     # Default search type when no specific trigger

LTM_EMOTIONAL_SEARCH_THRESHOLD = 0.7



# ========================================
# LTM CLEANUP AND RETENTION
# ========================================

# Retention policy
LTM_CLEANUP_ENABLED = True                      # Enable automatic cleanup
LTM_RETENTION_DAYS = 365                        # Keep memories for 1 year
LTM_RETENTION_MIN_IMPORTANCE = 0.8              # Min importance to keep after retention period
LTM_RETENTION_CRITICAL_IMPORTANCE = 0.95        # Critical memories - never delete
LTM_RETENTION_MIN_ACCESS_COUNT = 5              # Keep if accessed >= N times regardless of age

# Cleanup execution
LTM_CLEANUP_BATCH_SIZE = 1000                   # Delete in batches to avoid long locks
LTM_CLEANUP_QUERY_TIMEOUT = 30.0                # Timeout for cleanup queries (seconds)
LTM_CLEANUP_SCHEDULE_HOUR = 3                   # Hour to run cleanup (UTC)
LTM_CLEANUP_SCHEDULE_MINUTE = 0                 # Minute to run cleanup
LTM_CLEANUP_DRY_RUN = False                     # If True, only log what would be deleted

# Summary generation
LTM_SUMMARY_ENABLED = True                      # Generate summaries before deletion
LTM_SUMMARY_PERIOD = 'month'                    # Aggregation period: 'week', 'month', 'quarter'
LTM_SUMMARY_MIN_MEMORIES = 5                    # Min memories to create summary
LTM_SUMMARY_TOP_EMOTIONS = 5                    # Number of top emotions to store
LTM_SUMMARY_TOP_TAGS = 10                       # Number of top tags to store

# Cache invalidation after cleanup
LTM_CLEANUP_INVALIDATE_CACHE = True             # Clear novelty caches after cleanup
LTM_CLEANUP_INVALIDATE_PATTERNS = [             # Cache patterns to invalidate
    "novelty:knn:*",
    "novelty:temporal:*", 
    "novelty:final:*"
]

# Logging and monitoring
LTM_CLEANUP_LOG_LEVEL = 'INFO'                  # Logging level for cleanup operations
LTM_CLEANUP_EMIT_EVENTS = True                  # Generate events for Event Store



# ========================================
# МЕТАДАННЫЕ ДЛЯ ЛОГИКИ ПОИСКА
# ========================================

# Приоритеты категорий (для определения search_type)
LTM_TRIGGER_PRIORITIES = {
    'self_related': 1,        # Высший приоритет - всегда self_related search
    'unfinished_business': 2, # Высокий - часто нужен vector search
    'memory_recall': 2,       # Высокий - explicit memory request
    'uncertainty_doubt': 3,   # Высокий-средний - нужна поддержка из памяти
    'emotional_resonance': 3, # Средний
    'temporal_acute': 3,      # Средний 
    'existential_inquiry': 4, # Низкий
    'pattern_recognition': 4, # Низкий
    'metacognitive': 4,       # Низкий
    'temporal_distant': 5,    # Самый низкий
    'contextual_amplifiers': 5  # Самый низкий
}

# Маппинг категорий на типы поиска  
LTM_CATEGORY_TO_SEARCH_TYPE = {
    'self_related': 'self_related',
    'memory_recall': 'recent',        # Explicit requests often want recent memories
    'past_reference': 'recent',
    'unfinished_business': 'vector',  # Complex semantic search needed
    'uncertainty_doubt': 'vector',    # Need semantically similar situations for support
    'emotional_resonance': 'vector',  # Emotional semantic similarity
    'existential_inquiry': 'vector',  # Deep meaning connections
    'temporal_acute': 'recent',       # Recent time = recent search
    'temporal_distant': 'importance', # Old time = important memories only
    'pattern_recognition': 'vector',  # Pattern matching needs semantics
    'metacognitive': 'vector',        # Thinking patterns need semantics  
    'contextual_amplifiers': 'vector' # Context needs semantic analysis
}

