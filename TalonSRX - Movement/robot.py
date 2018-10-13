import wpilib
from wpilib.drive import DifferentialDrive
from ctre import WPI_TalonSRX

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        '''Robot initialization function'''

        # object that handles basic drive operations
        self.motor1 = WPI_TalonSRX(1)
        self.motor2 = WPI_TalonSRX(2)

        self.drive = wpilib.drive.DifferentialDrive(self.motor1, self.motor2)

        # joysticks 1 & 2 on the driver station
        #self.motor1 = WPI_TalonSRX(2)
        self.stick = wpilib.Joystick(0)


    def teleopPeriodic(self):
        '''Runs the motors with tank steering'''
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())


if __name__ == '__main__':
    wpilib.run(MyRobot)