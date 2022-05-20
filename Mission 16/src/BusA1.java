import java.util.Random;

/**
 * Represents the NUS Bus A1.
 */
public class BusA1 extends AbstractBus {

    public BusA1() {
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("A1", null);
        assert pair != null;
        currentStopName = pair.stopName; // assigns to superclass' `stopName`
    }

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If
     * the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop;
     *         else, -1.
     */
    @Override
    public int moveToNextStop() {
        // TODO: Implement this (Task 2a)
        BusMap.Pair nextstop = BusMap.getNextStopAndTimeTaken("A1", currentStopName);
        this.currentStopName = nextstop.stopName;
        if (nextstop.timeTakenFromPreviousStop = null) {
            return -1;
        } else {
            return nextstop.timeTakenFromPreviousStop;
        }
    }

    // Bus A1 should breakdown with a probability of 0.1
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        return false;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return null;
    }

}
