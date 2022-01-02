program test;
var
    A : real;
    C : real;

function sum(num : integer) : real;
begin
    if num = 1 then
    begin
        sum := num + 25.3;
    end
    else
    begin
        sum := 100;
    end;
end;

begin
    A := 1;
    C := sum(A);
end.