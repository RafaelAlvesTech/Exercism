<?php

class Lasagna
{
    public function timeToLayer()
    {
        // Implement the expectedCookTime method
        return 2;
    }
    public function expectedCookTime()
    {
        // Implement the expectedCookTime method
        return 40;
    }

    public function remainingCookTime($elapsed_minutes)
    {
        return $this->expectedCookTime() - $elapsed_minutes;
    }

    public function totalPreparationTime($layers_to_prep)
    {
        return $layers_to_prep * $this->timeToLayer();
    }

    public function totalElapsedTime($layers_to_prep, $elapsed_minutes)
    {
        return $this->totalPreparationTime($layers_to_prep) - ($this->remainingCookTime($elapsed_minutes)) + $this->expectedCookTime();
    }

    public function alarm()
    {
        return "Ding!";
    }
}
