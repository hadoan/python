using System;
using System.Net.Mqtt;
using System.Text;
using System.Threading.Tasks;

namespace mqtt_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            //TestReceiveMqtt().Wait();
            TestSendMqtt().Wait();
            Console.WriteLine("Press Enter to continue...");
            Console.ReadLine();
        }

        private static async Task TestReceiveMqtt()
        {

            var configuration = new MqttConfiguration();
            var client = await MqttClient.CreateAsync("localhost", configuration);

            var sessionState = await client.ConnectAsync(new MqttClientCredentials(clientId: "hatest"));
            await client.SubscribeAsync("house/light", MqttQualityOfService.AtLeastOnce); //QoS0

            client.MessageStream.Subscribe(x => Console.WriteLine($"Message {x.Payload} received in topic {x.Topic}"));


        }

        private static async Task TestSendMqtt()
        {

            var configuration = new MqttConfiguration();
            var client = await MqttClient.CreateAsync("localhost", configuration);

            var sessionState = await client.ConnectAsync(new MqttClientCredentials(clientId: "hatest"));
            //await client.SubscribeAsync("house/light", MqttQualityOfService.AtLeastOnce); //QoS0

            //client.MessageStream.Subscribe(x => Console.WriteLine($"Message {x.Payload} received in topic {x.Topic}"));
            var message1 = new MqttApplicationMessage("house/light", Encoding.UTF8.GetBytes("Foo Message 1"));

            await client.PublishAsync(message1, MqttQualityOfService.AtLeastOnce);

        }
    }
}
