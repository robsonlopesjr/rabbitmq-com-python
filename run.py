from src.main.rabbitmq_configs.consumer import RabbitMQPConsumer

if __name__ == "__main__":
    consumer = RabbitMQPConsumer()
    consumer.start()
