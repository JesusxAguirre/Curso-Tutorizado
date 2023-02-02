<?php

class Thesaurus
{
    private $thesaurus;

    function __construct(array $thesaurus)
    {
        $this->thesaurus = $thesaurus;
    }

    public function getSynonyms(string $word) : string
    {
        $arr = array();
        if(array_key_exists($word,$this->thesaurus)){
        $arr = array("word"=>$word,"synonyms"=>$this->thesaurus[$word]);
        $json = json_encode($arr);
        }else{
      $arr = array("word" => $word, "stnonyms" => []);
        }
        
        return $json;
    }
}

$thesaurus = new Thesaurus(
    [
        "buy" => array("purchase"),
        "big" => array("great", "large")
    ]
);

echo $thesaurus->getSynonyms("big");
echo "\n";
echo $thesaurus->getSynonyms("agelast");

?>