from enum import Enum


class TrafficLightState(Enum):
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    
class TrafficLightFSM:
    def __init__(self):
        self.state = TrafficLightState.RED
    
    def transition(self):
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW
        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.RED

    def __str__(self):
        return f"Current State: {self.state.value}"


if __name__ == "__main__":
    fsm = TrafficLightFSM()
    for _ in range(6):
        print(fsm)
        fsm.transition()
        
