import time
import sys
from src.lcd import lcd_write


def print_banner():
    lcd_write("Attendance System")
    lcd_write("Loading...")
    print("""\n
**********************************************************************************************
*                                                                                            *
*    ____  _____ ___ ____       _  _____ _____ _____ _   _ ____    _    _   _  ____ _____    *
*   |  _ \|  ___|_ _|  _ \     / \|_   _|_   _| ____| \ | |  _ \  / \  | \ | |/ ___| ____|   *
*   | |_) | |_   | || | | |   / _ \ | |   | | |  _| |  \| | | | |/ _ \ |  \| | |   |  _|     *
*   |  _ <|  _|  | || |_| |  / ___ \| |   | | | |___| |\  | |_| / ___ \| |\  | |___| |___    *
*   |_| \_\_|   |___|____/  /_/   \_\_|   |_| |_____|_| \_|____/_/   \_\_| \_|\____|_____|   *
*                                                                                            *
*         | B.Tech Project 2022 | Dept of Electronics & Communication Engg. | RCEE  |        *
*                                                                                            *
*                                                                                            *
* Team Members                                                      Mentor                   *
*  > 18ME1A04G8 - V Jyoshitha                                       > A.N.L Harisha          *
*  > 18ME1A04G3 - U Sai Kiran                                                                *
*  > 18ME1A04F4	- T Charturya                                                                *
*  > 18ME1A04E6	- SK Nagulmeera                                                              *
*                                                                                            *
*                                                                                            *
* Year: IV                            Section: C                                Branch: ECE  *
**********************************************************************************************\n""")


def loading():
    print(" "*44+"Loading:")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    for i in range(len(animation)):
        time.sleep(0.3)
        sys.stdout.write("\r" + " "*42 + animation[i % len(animation)])
        sys.stdout.flush()
    
    print("\n")

