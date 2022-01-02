program test;
var
    A : real;
    B : integer;
    C : real;

function sum(num : integer; real1 : real) : real;
begin
    if num = 1 then
    begin
        sum := num + real1;
    end
    else
    begin
        sum := 100;
    end;
end;

begin
    A := 1;
    B := 20;
    C := sum(A, B);
    writeLn
end.