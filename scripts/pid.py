#!/usr/bin/python

import time
import numpy as np


class PID:
    def __init__(
        self,
        Kp=0.0,
        Ki=0.0,
        Kd=0.0,
        set_point=0.0,
        sample_time=0.01,
        out_limits=(None, None),
    ):

        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.p_term = 0.0
        self.i_term = 0.0
        self.d_term = 0.0

        self.set_point = set_point

        self.sample_time = sample_time

        self.out_limits = out_limits

        self.last_err = 0.0

        self.last_time = None

        self.output = 0.0

    def update(self, feedback_val):
        """Compute PID control value based on feedback_val.
        """

        curr_time = time.time()

        if self.last_time is None:
            self.last_time = curr_time
            de = 0
        else:
            de = (feedback_val - self.last_err) / (curr_time - self.last_time)

        # if abs(feedback_val - self.last_err) > 0.5:
        #     de = 0

        self.i_term += (feedback_val * (curr_time - self.last_time))*self.Ki

        self.last_err = feedback_val
        self.last_time = curr_time
        self.d_term = de

        output = self.Kp * feedback_val + self.i_term + self.Kd * self.d_term

        if self.out_limits[0] is not None and self.out_limits[1] is not None:
            if output > self.out_limits[1]:
                self.i_term -= (output - self.out_limits[1])
                output = self.out_limits[1]
            elif output < self.out_limits[0]:
                self.i_term += (self.out_limits[0] - output)
                output = self.out_limits[0]

        return output

    def __call__(self, feeback_val):
        return self.update(feeback_val)
