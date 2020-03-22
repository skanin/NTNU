public class Unit {

    private final String symbol;
    private final Unit base;
    private final double factor, offset;

    public Unit(String symbol, Unit base, double factor, double offset) throws IllegalArgumentException {
        if(symbol.matches(".*\\d.*")) throw new IllegalArgumentException("Can only contain letters");

        this.symbol = symbol;
        this.base = base;
        this.factor = factor;
        this.offset = offset;
    }

    public Unit(String symbol) throws IllegalArgumentException {
        this(symbol, null, null, null);
    }


}
