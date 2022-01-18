program exFunction;
var
   a, b, ret : integer;
   c : string;

function max(num1, num2: integer; name_string : string): integer;
var
   result: integer;
begin
   if num1 > num2 then
        begin
        if num1 < 1000 then
            result := 2000
        else
            result := num2;
        end
    else
        result := num1;
   max := result;
end;

begin
   a := 100;
   b := 200;
   c := 'hej';
   ret := max(a, b, c);
end.