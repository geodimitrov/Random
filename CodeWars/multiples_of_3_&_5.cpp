int solution(int number)
{
  int sumMultiples = 0;

  for (int i = 1; i < number; i ++){

    if (i % 3 == 0 || i % 5 == 0){
        sumMultiples += i;
    }
  }
  return sumMultiples;
}