class FileExample {
   static void main(String[] args) {
      new File("H:\\Scripts\\report").eachFile() { file->
         println file.getAbsolutePath()
      }
   }
}