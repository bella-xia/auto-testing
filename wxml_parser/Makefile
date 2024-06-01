CXX_SRCS = utils.cpp HTMLToken.cpp HTMLTokenizer.cpp WXMLDocumentParser.cpp test_script.cpp
CXX_OBJS = $(CXX_SRCS:%.cpp=%.o)

CXX_TOKENIZE_SRCS = utils.cpp HTMLToken.cpp HTMLTokenizer.cpp test_script.cpp
CXX_TOKENIZE_OBJS = $(CXX_SRCS:%.cpp=%.o)

CXX = g++ 
CXXFLAGS =  -g -Wall -std=c++17

%.o : %.cpp
	$(CXX) $(CXXFLAGS) -c $<

all : parse

parse : $(CXX_OBJS)
	$(CXX) -o $@ $(CXX_OBJS)

tokenize : $(CXX_TOKENIZE_OBJS)
	$(CXX) -o $@ $(CXX_TOKENIZE_OBJS)

clean :
	rm -f *.o tokenize parse depend.mak

depend :
	$(CXX) $(CXXFLAGS) -M $(CXX_SRCS) >> depend.mak

depend.mak :
	touch $@

solution.zip : 
	zip -9r *.cpp *.h

include depend.mak