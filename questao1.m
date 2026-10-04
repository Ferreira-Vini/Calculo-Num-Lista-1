% Valores de x que a questão pede
x = [1e-15, 1e+15];

% Calculando a expressão
% Usamos ./ para ele fazer a conta para os dois valores de x de uma vez
valor_calculado = ((1 + x) - 1) ./ x;

% O valor exato matemático. 
% Se você cortar (1 - 1), sobra x / x, que sempre dá 1.
valor_exato = [1, 1];

% Fórmulas do erro absoluto e relativo
erro_absoluto = abs(valor_exato - valor_calculado);
erro_relativo = erro_absoluto ./ abs(valor_exato);

% Imprimindo os resultados no painel de baixo (Command Window)
disp('Valores calculados (para 1e-15 e 1e+15):')
disp(valor_calculado)

disp('Erro Absoluto:')
disp(erro_absoluto)

disp('Erro Relativo:')
disp(erro_relativo)