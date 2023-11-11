public class FizzBuzz
{

    private int _printerIndex = 1;
    private readonly int _n;

    public FizzBuzz(int n) {
        _n = n;
    }

    private void WaitForPrinterIndexAndIncrement(int i, Action action)
    {
        if (_printerIndex < i)
            System.Threading.SpinWait.SpinUntil(() => _printerIndex == i);

        action();
        _printerIndex += 1;
    }

    public void Fizz(Action printFizz)
    {
        for (var i = 1; i <= _n; i++)
        {
            if (i % 3 == 0 && i % 5 != 0)
                WaitForPrinterIndexAndIncrement(i, printFizz);
        }
    }

    public void Buzz(Action printBuzz)
    {
        for (var i = 1; i <= _n; i++)
        {
            if (i % 3 != 0 && i % 5 == 0)
                WaitForPrinterIndexAndIncrement(i, printBuzz);
        }
    }

    public void Fizzbuzz(Action printFizzBuzz) 
    {
        for (var i = 1; i <= _n; i++)
        {
            if (i % 15 == 0)
                WaitForPrinterIndexAndIncrement(i, printFizzBuzz);
        }
    }

    public void Number(Action<int> printNumber) 
    {
        for (var i = 1; i <= _n; i++)
        {
            var iCopy = i; 
            if (i % 3 != 0 && i % 5 != 0)
                WaitForPrinterIndexAndIncrement(i, () => printNumber(iCopy));
        }
    }
}