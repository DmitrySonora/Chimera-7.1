"""
События для анализа стиля общения и черт личности
"""
from typing import Optional, Dict, Any, List
from actors.events.base_event import BaseEvent


class PersonalityTraitDetectedEvent(BaseEvent):
    """Событие обнаружения проявления черты личности Химеры"""
    
    @classmethod
    def create(cls,
               user_id: str,
               trait_name: str,
               strength: float,
               context_mode: str,
               confidence: float,
               trigger_markers: List[str],
               message_preview: str,
               correlation_id: Optional[str] = None) -> 'PersonalityTraitDetectedEvent':
        """
        Создать событие обнаружения черты личности
        
        Args:
            user_id: ID пользователя
            trait_name: Название черты (curiosity, irony, empathy и т.д.)
            strength: Сила проявления (0.0-1.0)
            context_mode: Режим общения (talk/expert/creative)
            confidence: Уверенность в детекции (0.0-1.0)
            trigger_markers: Сработавшие лингвистические маркеры
            message_preview: Фрагмент текста где обнаружено (max 100 символов)
            correlation_id: ID корреляции для связывания событий
        """
        return cls(
            stream_id=f"personality_{user_id}",
            event_type="PersonalityTraitDetectedEvent",
            data={
                "user_id": user_id,
                "trait_name": trait_name,
                "strength": strength,
                "context_mode": context_mode,
                "confidence": confidence,
                "trigger_markers": trigger_markers,
                "message_preview": message_preview[:100] + "..." if len(message_preview) > 100 else message_preview
            },
            version=0,
            correlation_id=correlation_id
        )


class StyleVectorUpdatedEvent(BaseEvent):
    """Событие обновления стилевого вектора пользователя"""
    
    @classmethod
    def create(cls,
               user_id: str,
               old_vector: Dict[str, float],
               new_vector: Dict[str, float],
               messages_analyzed: int,
               significant_change: bool,
               dominant_style: str,
               correlation_id: Optional[str] = None) -> 'StyleVectorUpdatedEvent':
        """
        Создать событие обновления стиля общения
        
        Args:
            user_id: ID пользователя
            old_vector: Предыдущий вектор стиля (если был) - словарь с 4 компонентами
            new_vector: Новый вектор стиля - словарь с 4 компонентами
            messages_analyzed: Количество проанализированных сообщений
            significant_change: Изменение > 20% хотя бы по одной компоненте
            dominant_style: Доминирующий стиль (playful/serious/emotional/creative)
            correlation_id: ID корреляции
        """
        return cls(
            stream_id=f"personality_{user_id}",
            event_type="StyleVectorUpdatedEvent",
            data={
                "user_id": user_id,
                "old_vector": old_vector,
                "new_vector": new_vector,
                "messages_analyzed": messages_analyzed,
                "significant_change": significant_change,
                "dominant_style": dominant_style
            },
            version=0,
            correlation_id=correlation_id
        )


class PartnerPersonaUpdatedEvent(BaseEvent):
    """Событие обновления модели собеседника (Partner Persona)"""
    
    @classmethod
    def create(cls,
               user_id: str,
               persona_id: str,
               version: int,
               previous_mode: Optional[str],
               recommended_mode: str,
               confidence_score: float,
               prediction_data: Optional[Dict[str, Any]],
               reason: str,
               correlation_id: Optional[str] = None) -> 'PartnerPersonaUpdatedEvent':
        """
        Создать событие обновления Partner Persona
        
        Args:
            user_id: ID пользователя
            persona_id: UUID персоны (как строка)
            version: Версия персоны (не путать с version события!)
            previous_mode: Предыдущий рекомендованный режим (если был)
            recommended_mode: Новый рекомендованный режим (talk/expert/creative)
            confidence_score: Уверенность в рекомендации (0.0-1.0)
            prediction_data: Данные предсказания (predicted_interests, prediction_confidence и т.д.)
            reason: Причина обновления (scheduled/significant_change/manual)
            correlation_id: ID корреляции
        """
        return cls(
            stream_id=f"personality_{user_id}",
            event_type="PartnerPersonaUpdatedEvent",
            data={
                "user_id": user_id,
                "persona_id": persona_id,
                "version": version,
                "previous_mode": previous_mode,
                "recommended_mode": recommended_mode,
                "confidence_score": confidence_score,
                "prediction_data": prediction_data,
                "reason": reason
            },
            version=0,
            correlation_id=correlation_id
        )


class TraitManifestationEvent(BaseEvent):
    """Событие проявления черты личности в конкретном контексте"""
    
    @classmethod
    def create(cls,
               user_id: str,
               trait_name: str,
               manifestation_id: str,
               intensity: float,
               emotional_context: Dict[str, float],
               mode: str,
               response_fragment: str,
               timestamp_utc: str,
               correlation_id: Optional[str] = None) -> 'TraitManifestationEvent':
        """
        Создать событие проявления черты в контексте
        
        Args:
            user_id: ID пользователя
            trait_name: Название черты
            manifestation_id: UUID проявления (как строка)
            intensity: Интенсивность проявления (0.0-1.0)
            emotional_context: Эмоциональный контекст момента (словарь эмоций и их значений)
            mode: Режим общения (talk/expert/creative)
            response_fragment: Фрагмент ответа Химеры (max 200 символов)
            timestamp_utc: Время в ISO формате
            correlation_id: ID корреляции
        """
        return cls(
            stream_id=f"personality_{user_id}",
            event_type="TraitManifestationEvent",
            data={
                "user_id": user_id,
                "trait_name": trait_name,
                "manifestation_id": manifestation_id,
                "intensity": intensity,
                "emotional_context": emotional_context,
                "mode": mode,
                "response_fragment": response_fragment[:200] + "..." if len(response_fragment) > 200 else response_fragment,
                "timestamp_utc": timestamp_utc
            },
            version=0,
            correlation_id=correlation_id
        )