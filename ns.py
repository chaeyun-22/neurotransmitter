class nervous_disease():
    
    def __init__(self, name, neurotransmitter, concentration):
        self.name = name
        self.neurotransmitter = neurotransmitter
        self.concentration = concentration

    def patient_info(self):
        print(f"환자 이름: {self.name}, 신경 전달 물질 종류: {self.neurotransmitter}, 수치: {self.concentration}")

    