type file;
file fmapper <"wordcount/Mapper.py">;
file freducer <"wordcount/Reducer.py">;
app (file cout) map (file pyfile, file datafile)
{
	python @pyfile @datafile stdout=@filename(cout);
}

app (file cout) reduce (file pyfile, file intermediatefile)
{
	python @pyfile @intermediatefile stdout=@filename(cout);
}

file inputfile <single_file_mapper; file="input/dataset">;
file cout <"output/intermediate.txt">;
cout = map (fmapper, inputfile);

file cout2 <"output/WordCount-swift.txt">;
cout2 = reduce (freducer,cout);

