CREATE TYPE measure as ENUM ('bodytemp','systolic','diastolic', 'bpm', 'sato2', 'ferritina', 'hemoglobina');




INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (1, 'Carlos Ferreira', '1956-03-30', '919876543', 'M');
INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (2, 'Rui Turquel', '1953-10-20', '919876543', 'M');
INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (3, 'Filipe Pereira', '1932-06-30', '919876543', 'M');
INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (4, 'Jorge Pereira', '1938-06-27', '919876543', 'M');
INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (5, 'Joana Silveira', '1963-03-10', '919876543', 'F');
INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (6, 'Sara Silves', '1972-02-27', '919876543', 'F');
INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (7, 'Mariana Teixeira', '1954-07-31', '919876543', 'F');
INSERT INTO public.paciente (nr_utente, nome, dtanasc, contacto, genero) VALUES (8, 'Rosa Santos', '1952-08-01', '919876543', 'F');


INSERT INTO public.servico (codservico, descricao) VALUES ('UCI-I', 'Unidade de Cuidados Intensivos - I');
INSERT INTO public.servico (codservico, descricao) VALUES ('UCI-II', 'Unidade de Cuidados Intensivos - II');
INSERT INTO public.servico (codservico, descricao) VALUES ('UCI-III', 'Unidade de Cuidados Intensivos - III');


INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000000, '2025-02-19', 100, 100, null, 'UCI-I');
INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000001, '2025-02-11', 101, 101, null, 'UCI-I');
INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000002, '2025-02-18', 102, 102, null, 'UCI-I');
INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000003, '2025-02-17', 103, 103, null, 'UCI-I');
INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000004, '2025-02-14', 104, 104, null, 'UCI-II');
INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000005, '2025-02-15', 105, 105, null, 'UCI-II');
INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000006, '2025-02-18', 106, 106, null, 'UCI-II');
INSERT INTO public.internamento (episodio, data_admissao, cama, id_paciente, data_alta, id_servico) VALUES (10000007, '2025-02-17', 107, 107, null, 'UCI-II');