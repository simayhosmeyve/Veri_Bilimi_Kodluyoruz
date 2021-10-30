### Proje 1
* [16,21,11,8,12,22] -> Merge Sort

>Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.

             [16,21,11,8,12,22]
        [16,21,11]        [8,12,22]
      [16]  [21,11]      [8]   [12,22]
           |                  |
      [16] [11,21]       [8] [12,22]    n-1 
       [11,16,21]         [8,12,22]     n-1
            [8,11,12,16,21,22]          n-1

O(n) = nlogn