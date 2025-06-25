# Fox Chicken Grain Program

This is a program I have done in school as a set project. You need to get all of the things to the other side without losing anything.

---

The main idea is:

 - If the Fox is with the Chicken, the fox eats the chicken.
 - If the Chicken is with the Grain, the chicken eats the grain.

---

**You have to**:

Get all to the other side without losing anything.

<details>
<summary>this is how you solve it</summary>

---

| Step | Left Bank           | Boat      | Right Bank        | Notes                                  |
|------|---------------------|-----------|-------------------|----------------------------------------|
| 1    | Farmer, Fox, Chicken, Grain | Farmer + Chicken | Fox, Grain         | Take Chicken over                    |
| 2    | Farmer, Fox, Grain  | Farmer    | Chicken           | Farmer returns alone                  |
| 3    | Farmer, Chicken, Grain | Farmer + Fox   | Chicken, Grain      | Take Fox over                        |
| 4    | Farmer, Chicken, Grain | Farmer + Chicken | Fox, Grain         | Bring Chicken back                   |
| 5    | Farmer, Grain       | Farmer + Grain  | Fox, Chicken        | Take Grain over                      |
| 6    | Farmer              | Farmer    | Fox, Chicken, Grain | Farmer returns alone                  |
| 7    | Farmer + Chicken    |           | Fox, Grain, Chicken| Take Chicken over (final trip)        |

At the end, all items have made it safely to the other side!

---

</details>
