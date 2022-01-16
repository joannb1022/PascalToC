program exFunction;
var
   a, b, ret : integer;

function max(num1, num2: integer): integer;
var
  a: integer;
begin
    if num1 < 20 then
        a := 10
    else
        while a < 400 do
            a := a + 100;
end;
begin
   a := 100;
   b := 200;
   ret := max(a, b);
end.