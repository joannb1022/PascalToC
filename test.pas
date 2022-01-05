program test;
var
    AB, TT : real;

function sum(num : real) : real;
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
    AB := 1;
    TT := sum(AB);
end.