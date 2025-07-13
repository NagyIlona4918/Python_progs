"""Ranges and descriptions with ChatGPT's help:"""

class_a_range = (1, 126)      # 1.0.0.0 – 126.255.255.255
class_b_range = (128, 191)    # 128.0.0.0 – 191.255.255.255
class_c_range = (192, 223)    # 192.0.0.0 – 223.255.255.255
class_d_range = (224, 239)    # 224.0.0.0 – 239.255.255.255
class_e_range = (240, 255)    # 240.0.0.0 – 255.255.255.255

class_a_description = "Reserved for large networks (e.g., ISPs, large organizations)"
class_b_description = "Used by medium-sized networks (e.g., universities, government)"
class_c_description = "Used for small networks (e.g., private companies, homes)"
class_d_description = "Reserved for multicast (one-to-many communication)"
class_e_description = "Reserved for experimental or future use"

def ip_adress_classify():

    ranges = [
        class_a_range,
        class_b_range,
        class_c_range,
        class_d_range,
        class_e_range
    ]

    descriptions = [
        class_a_description,
        class_b_description,
        class_c_description,
        class_d_description,
        class_e_description
    ]
    
    class_labels = ["A", "B", "C", "D", "E"]

    ip_classes = {
        label: {"range": one_range, "description": description}
        for label, one_range, description in zip(class_labels, ranges, descriptions)
    }

    ip_address = input("Write the IP address: (x.x.x.x/x)").strip().split('.')
    starts_with = int(ip_address[0])

    for label, data in ip_classes.items():
        min_range, max_range = data["range"]
        if min_range <= starts_with <= max_range:
            print(f'The class of your IP address: {label}')
            return

ip_adress_classify()