brew install mosquitto
brew services start mosquitto
brew services info mosquitto

mosquitto_sub -h localhost -t test_topic
mosquitto_pub -h localhost -t test_topic -m "Hello, MQTT!"

mosquitto has been installed with a default configuration file.
You can make changes to the configuration by editing:
    /opt/homebrew/etc/mosquitto/mosquitto.conf

To start mosquitto now and restart at login:
  brew services start mosquitto
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mosquitto/sbin/mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf

# for static IP
sudo nano /etc/dhcpcd.conf

interface <interface_name>
static ip_address=<desired_static_ip>/24
static routers=<router_ip>
static domain_name_servers=<dns_server_ip>

interface eth0
static ip_address=192.168.1.10/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8

sudo service dhcpcd restart
ip addr show <interface_name>
