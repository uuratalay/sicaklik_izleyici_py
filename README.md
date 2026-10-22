# sicaklik_izleyici_py

ROS2 (Humble, ament_python) ile yazılmış, basit bir sıcaklık izleme sistemi
ödevi. İki düğümden oluşur:

- **sensor_node** (`sensor.py`): her 1 saniyede bir 20.0–40.0 °C arası
  rastgele bir değer üretip `std_msgs/Float32` olarak `/sicaklik` topic'ine
  yayınlar.
- **izleyici_node** (`izleyici.py`): `/sicaklik` topic'ine abone olur, gelen
  her değeri `get_logger().info()` ile loglar; değer eşik üzerindeyse
  `get_logger().warn()` ile uyarı verir. Eşik değeri `esik` adlı bir
  ROS2 parametresidir (varsayılan `30.0`), koda sabit yazılmamıştır.

## Gereksinimler

- ROS2 Humble (Ubuntu 22.04 / Jammy)
- `rclpy`, `std_msgs` (standart ROS2 kurulumuyla gelir)

## Kurulum ve derleme

```bash
# workspace'e kopyala/klonla (örnek yol)
cd ~/ros2_ws/src
# (bu paket zaten burada değilse git clone ile ekleyin)

cd ~/ros2_ws
colcon build --packages-select sicaklik_izleyici_py
source install/setup.bash
```

## Çalıştırma

İki ayrı terminalde (her ikisinde de `source install/setup.bash` yapılmış
olmalı):

```bash
# Terminal 1
ros2 run sicaklik_izleyici_py sensor

# Terminal 2
ros2 run sicaklik_izleyici_py izleyici
```

`izleyici` terminalinde her saniye bir `Alinan sicaklik: ...` INFO logu,
değer 30.0'ı geçtiğinde ayrıca sarı renkli bir `WARN` logu görünmelidir.

## Bonus: eşik değerini parametre ile değiştirme

Varsayılan eşik 30.0'dır. Farklı bir eşikle çalıştırmak için:

```bash
ros2 run sicaklik_izleyici_py izleyici --ros-args -p esik:=25.0
```

Bu örnekte eşik 25.0'a düşürüldüğü için daha fazla WARN logu görülecektir.

## Node-topic grafiği

Her iki düğüm de çalışırken aşağıdaki komutla grafiği görüntüleyip
`rqt_graph.png` olarak kaydedin:

```bash
rqt_graph
```

Beklenen bağlantı: `sensor_node` → `/sicaklik` → `izleyici_node`.

> Not: `rqt_graph.png` bu depoda yer tutucu olarak boş bırakılmıştır; gerçek
> ROS2 ortamında yukarıdaki adımları çalıştırıp kendi ekran görüntünüzle
> değiştirin.
