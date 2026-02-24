# Таблица-реестр событий Saga-хореографии оформления заказа
|Этап|Тип события|Название|
|:--|:--|:--|
|Заказ подтвержден пользователем|Domain|OrderConfirmedByUser|
|Товары на складе зарезервированы|Domain|ProductsReserved|
|Ошибка резервации товаров|Failure|ReservationFailed|
|Оплата прошла успешно|Domain|PaymentSucceded|
|Ошибка при попытке оплаты|Failure|PaymentFailed|
|Резервация товаров отменена|Compensation|ReservationCanceled|
|Заявка на доставку создана|Domain|DeliveryRequestCreated|
|Доставка одобрена службой доставки|Domain|DeliveryRequestConfirmed|
|Служба доставки отклонила заявку|Failure|DeliveryRequestCanceled|
|Средства возвращены|Compensation|RefundSucceded|
|Товар доставлен|Domain|OrderDelivered|
|Товар не удалось доставить|Failure|OrderDeliveryFailed|
|Товары возвращены на склад|Compensation|ProductsReturnedToStock|