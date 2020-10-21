from tkinter import *
import webbrowser


def class12():
    def chemistrylinks():
        root.destroy()

        chemistry = Tk()
        chemistry.title("Chemistry")
        chemistry.geometry("800x650")
        chemistry.configure(background="black")

        chapter1 = Button(chemistry, text="The solid state",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=a5WfQ7mSLBI&list=PLbu_fGT0MPsuJoldXfEROqx5oRXwQcaa5'))
        chapter2 = Button(chemistry, text="Solutions",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=nn-1UU_1PX8&list=PLF_7kfnwLFCHJ6kUboe60izCndyBUjiaZ'))
        chapter3 = Button(chemistry, text="Electrochemistry",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=j7PYqR1iGMg&list=PLF_7kfnwLFCF_VxKKAhHSLryCsJr3GW71'))
        chapter4 = Button(chemistry, text="Chemical kinetics",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Ez2EaGNt-u8&list=PLF_7kfnwLFCHlh8wdeQ_ZZ96DhBDjqGMZ'))
        chapter5 = Button(chemistry, text="surface chemistry",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Ez2EaGNt-u8&list=PLF_7kfnwLFCHlh8wdeQ_ZZ96DhBDjqGMZ'))
        chapter6 = Button(chemistry, text="General principles and processes of isolation of elements",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=juCvs-BNLbA&list=PLzSTglXGeoUsvwbg9f573_-GoNGe0eUJN'))
        chapter7 = Button(chemistry, text="THe p-block elements",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=wqHutdLBSCE&list=PLF_7kfnwLFCHzLy322Z87d5OBPNztukFs'))
        chapter8 = Button(chemistry, text="the d-block and f-block elements",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=nvAapFc_WgE&list=PLzSTglXGeoUvoWhQmJEV6-ScGn4tBTz2D'))
        chapter9 = Button(chemistry, text="coordination compounds",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=NDn_gZL2LTs&list=PLF_7kfnwLFCFVII1I1paHKCtq5VhlmAaC'))
        chapter10 = Button(chemistry, text="Haloalkanes and haloarenes",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=8OoPwXO110w&list=PLF_7kfnwLFCG-Fm0odaUEQjDTEHdyP3PP'))
        chapter11 = Button(chemistry, text="Alcohols, phenols and ether",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=IviTZ45FrJY&list=PLF_7kfnwLFCEllUy1_z114tXRmq7UQJlj'))
        chapter12 = Button(chemistry, text="Aldehydes, ketones and carboxylic acids",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=gKp1aM42VvI&list=PLF_7kfnwLFCHUtZnRiUbHrS5WSV0BsvSg'))
        chapter13 = Button(chemistry, text="Amines",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=SNoWfjyuwx8&list=PLbu_fGT0MPsvrWJD4Bz6fPIdqneiEyWIZ'))
        chapter14 = Button(chemistry, text="Biomolecules",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=moxsyv4WgRo&list=PLzSTglXGeoUtIcpKDCiw-N99IE7_SXdbQ'))
        chapter15 = Button(chemistry, text="Polymers",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=wL3s_Or2zhY&list=PLzSTglXGeoUuhXb4czCE_0fA2tQPA1yEk'))
        chapter16 = Button(chemistry, text="Chemistry in everyday life",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=oByTE_nXpEI'))

        chapter1.pack(pady=7)
        chapter2.pack(pady=7)
        chapter3.pack(pady=7)
        chapter4.pack(pady=7)
        chapter5.pack(pady=7)
        chapter6.pack(pady=7)
        chapter7.pack(pady=7)
        chapter8.pack(pady=7)
        chapter9.pack(pady=7)
        chapter10.pack(pady=7)
        chapter11.pack(pady=7)
        chapter12.pack(pady=7)
        chapter13.pack(pady=7)
        chapter14.pack(pady=7)
        chapter15.pack(pady=7)
        chapter16.pack(pady=7)

        chemistry.mainloop()

    def physicslinks():
        root.destroy()

        physics = Tk()
        physics.title("Chemistry")
        physics.geometry("800x650")
        physics.configure(background="black")

        chapter1 = Button(physics, text="Electric charges and fields",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=m5VbK66a254&list=PLF_7kfnwLFCHjzvhflQjAOG97MgutH3Z5'))
        chapter2 = Button(physics, text="Electrostatic potential and capatance",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=KV5HL1AgLeY&list=PLF_7kfnwLFCFxjSU9HKYiq2K2cxbpf6mz'))
        chapter3 = Button(physics, text="Current electricity",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=IdAji34f7TE&list=PLF_7kfnwLFCFZ4OVmzjBSqMIAzDK_6b8f'))
        chapter4 = Button(physics, text="Moving charges and magnetism",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=pJtE71ox6UA&list=PLF_7kfnwLFCF8sjVSdxn3yWAghIgVnw26'))
        chapter5 = Button(physics, text="Magnetism and matter",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=zQwBW0HqEQA&list=PLF_7kfnwLFCGrBjDfBug1q5U3vULrIAOR'))
        chapter6 = Button(physics, text="Electromagnetic induction",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=svd52GIjvDU&list=PLF_7kfnwLFCE6mi_so22MJJ988uaHBJaQ'))
        chapter7 = Button(physics, text="Alternating current",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=0X2ZRsOqBms&list=PLF_7kfnwLFCELMB-TfYgbfAN2nuP-z4t5'))
        chapter8 = Button(physics, text="Electromagnetic waves",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=K9Fa4UW704g&list=PLF_7kfnwLFCEmTm6t7akZcPRExU6wuVAU'))
        chapter9 = Button(physics, text="Ray optics and optical instruments",
                                        command=lambda: webbrowser.open('https://www.youtube.com/watch?v=_nGZGo4gHGo&list=PLF_7kfnwLFCFxb0yvMYbPqzvZn2GN5aMw'))
        chapter10 = Button(physics, text="Wave optics",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=6vOzZ8esTSs&list=PLF_7kfnwLFCHr4eZATw4YURnGNr6mwF5R'))
        chapter11 = Button(physics, text="Dual nature of radiation and matter",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=2JYSVsXV3Ac&list=PLF_7kfnwLFCHG4i2ZBF25z4rKNMdn36dt'))
        chapter12 = Button(physics, text="Atoms",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=w1gxYuOihJ4&list=PLWx_9IrHkqauXxxrFQktuQFLZUBHSsw7s'))
        chapter13 = Button(physics, text="Nuclei",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=kyYFsXp4kcQ&list=PLF_7kfnwLFCH5Okd6hTPRfzc7sqIeG7Jc'))
        chapter14 = Button(physics, text="Semiconductor electronics: Materials, devices and simple circuits",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=tFzuhoElDi4&list=PLbu_fGT0MPstO4NmoeEBTNkYRZ0kPYFIV'))

        chapter1.pack(pady=10)
        chapter2.pack(pady=10)
        chapter3.pack(pady=10)
        chapter4.pack(pady=10)
        chapter5.pack(pady=10)
        chapter6.pack(pady=10)
        chapter7.pack(pady=10)
        chapter8.pack(pady=10)
        chapter9.pack(pady=10)
        chapter10.pack(pady=10)
        chapter11.pack(pady=10)
        chapter12.pack(pady=10)
        chapter13.pack(pady=10)
        chapter14.pack(pady=10)

        physics.mainloop()

    def mathslinks():
        root.destroy()

        maths = Tk()
        maths.title("Chemistry")
        maths.geometry("800x650")
        maths.configure(background="black")

        chapter1 = Button(maths, text="Relations and functions",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LIisbCyqdlE&list=PLbu_fGT0MPsulk5jpAkbkoyB5zh3g5Rzg'))
        chapter2 = Button(maths, text="Inverse trigonometry functions",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=RO-PG4yeayk&list=PLbu_fGT0MPsuebu593XpIwrspIMZG8EkO'))
        chapter3 = Button(maths, text="Matrices",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=bjFbZBER7Ew&list=PLbu_fGT0MPsssTQnaPbHz2Fzr3oye3aYd'))
        chapter4 = Button(maths, text="Determinants",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=bjFbZBER7Ew&list=PLbu_fGT0MPsssTQnaPbHz2Fzr3oye3aYd'))
        chapter5 = Button(maths, text="Continuity and differentiability",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=ok9f8Cm4-Ak&list=PLqjFFrfKcY5ymLMzicO4Gr0I_X-8uUd7x'))
        chapter6 = Button(maths, text="Application and derivatives",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=dIKDrWOXUGk&list=PLbu_fGT0MPstnfHLA7GaGxwJ6N1xtfAEA'))
        chapter7 = Button(maths, text="Integrals",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=i5hUQVwtock&list=PLbu_fGT0MPstBzAW5gGWLltksM_yAs3si'))
        chapter8 = Button(maths, text="Application of Integrals",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=AO5xftAnGys'))
        chapter9 = Button(maths, text="Differential equations",
                          command=lambda: webbrowser.open('https://www.youtube.com/watch?v=4PEb9O51fkg&list=PLbu_fGT0MPst47LS0wEIKZWxmHtWSUGYu'))
        chapter10 = Button(maths, text="vector algebra",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=jCQGiduTd78&list=PLbu_fGT0MPssNwsoy1gWwbQAsQM92o5__'))
        chapter11 = Button(maths, text="Three dimensional geometry",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=c3lU74jZYkg&list=PLbu_fGT0MPssMBwaqs27eW6mmKTRx9FE3'))
        chapter12 = Button(maths, text="Linear programming",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=SahH5zZFasg'))
        chapter13 = Button(maths, text="Probability",
                           command=lambda: webbrowser.open('https://www.youtube.com/watch?v=YwdFvjqmBRM'))

        chapter1.pack(pady=10)
        chapter2.pack(pady=10)
        chapter3.pack(pady=10)
        chapter4.pack(pady=10)
        chapter5.pack(pady=10)
        chapter6.pack(pady=10)
        chapter7.pack(pady=10)
        chapter8.pack(pady=10)
        chapter9.pack(pady=10)
        chapter10.pack(pady=10)
        chapter11.pack(pady=10)
        chapter12.pack(pady=10)
        chapter13.pack(pady=10)

        maths.mainloop()

    root = Tk()
    root.title("All course in one click")
    root.geometry("800x650")
    root.configure(background="black")

    chemistry = Button(root, text="Chemistry",  height=3,
                       width=20, command=chemistrylinks)
    physics = Button(root, text="Physics", height=3,
                     width=20, command=physicslinks)
    maths = Button(root, text="Maths", height=3, width=20, command=mathslinks)

    chemistry.configure(bg="red")
    physics.configure(bg="red")
    maths.configure(bg="red")

    chemistry.pack(pady=75)
    physics.pack(pady=75)
    maths.pack(pady=75)

    root.mainloop()


if __name__ == '__main__':
    class12()
